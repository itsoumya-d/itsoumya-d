#!/usr/bin/env python3
""""Ask my README" bot: answers an issue titled ``ask: <question>``.

Runs from .github/workflows/ask.yml on ``issues: opened``. It reads the issue
from the event payload (never from shell-interpolated strings), answers from
profile.json + the live data in skin/data.json, comments, labels the issue
``answered`` and closes it. The hourly build then counts answered issues.

Deterministic by design: no LLM, so nobody can talk it into inventing claims,
and it costs nothing to run.

Local dry run (prints the reply, touches nothing):
    python skin/answer.py --dry-run "ask: what's your strongest project?"
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build  # noqa: E402
import knowledge  # noqa: E402

MAX_Q = 300


def parse_question(title: str, body: str, labeled: bool = False) -> str | None:
    """Question text from an ``ask: ...`` title (or any title on an ``ask``-labelled issue)."""
    t = (title or "").strip()
    m = re.match(r"ask\s*[:\-]\s*", t, re.I)
    if m:
        q = t[m.end():].strip()
    elif labeled:
        q = t
    else:
        return None
    if not q:  # title left as "ask:" -> use the form's free-text field
        lines = [l.strip() for l in (body or "").splitlines()
                 if l.strip() and not l.startswith("###") and l.strip() != "_No response_"]
        q = " ".join(lines)
    return q[:MAX_Q] or None


def compose(profile: dict, live: dict, question: str, synced: str) -> tuple[str, str]:
    langs, _ = build.languages(live.get("repos") or {})
    ctx = {**live, "languages": langs}
    intents = knowledge.build_intents(profile, ctx)
    intent, md = knowledge.answer(profile, ctx, question, intents)
    login = profile["login"]
    footer = (f"\n\n---\n<sub>🤖 Answered automatically by [`skin/answer.py`](https://github.com/{login}/{login}/"
              f"blob/main/skin/answer.py) from live repo data (synced {synced}). Soumya is notified of every "
              f"question and may follow up here. To talk directly: [email](mailto:{profile['email']}) · "
              f"[LinkedIn]({profile['linkedin']}).</sub>")
    return intent, f"Thanks for asking! Here's the answer, built from live data:\n\n{md}{footer}"


def gh(method: str, path: str, body: dict | None = None):
    token = os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(
        f"https://api.github.com{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "Content-Type": "application/json", "User-Agent": "ask-my-readme"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read() or b"null")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", metavar="TITLE", help="answer a title locally and print it")
    args = ap.parse_args()

    profile = json.loads((HERE / "profile.json").read_text(encoding="utf-8"))
    data = json.loads((HERE / "data.json").read_text(encoding="utf-8"))
    live, synced = data.get("live") or {}, data.get("synced", "")

    if args.dry_run:
        q = parse_question(args.dry_run, "")
        if not q:
            print("not an ask: issue")
            return 0
        intent, reply = compose(profile, live, q, synced)
        print(f"[intent={intent}]\n{reply}")
        return 0

    event = json.loads(pathlib.Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
    issue = event.get("issue") or {}
    if issue.get("pull_request") or (issue.get("user") or {}).get("type") == "Bot":
        print("skip: not a human issue")
        return 0
    labeled = any(l.get("name") == "ask" for l in issue.get("labels") or [])
    q = parse_question(issue.get("title", ""), issue.get("body") or "", labeled)
    if not q:
        print("skip: not an ask: issue")
        return 0

    intent, reply = compose(profile, live, q, synced)
    repo, num = os.environ["GITHUB_REPOSITORY"], issue["number"]
    gh("POST", f"/repos/{repo}/issues/{num}/comments", {"body": reply})
    gh("POST", f"/repos/{repo}/issues/{num}/labels", {"labels": ["ask", "answered"]})
    gh("PATCH", f"/repos/{repo}/issues/{num}", {"state": "closed", "state_reason": "completed"})
    print(f"answered #{num} intent={intent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
