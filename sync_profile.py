"""Sync the profile README's auto-generated block.

Fetches, from public endpoints only:
  * the user's public GitHub repos (name, description, stars, last push)
  * the last CI run conclusion for each AI repo
  * the Hugging Face org's models/datasets/spaces (itssoumyad)

Then rewrites the text between
<!-- AUTO-START --> and <!-- AUTO-END --> in README.md.

Resilience: if a fetch fails (rate limits etc.), the previous row for that
item is kept instead of dropping it, so the block never degrades.
Uses GITHUB_TOKEN if set (CI provides a generous quota).
Usage: python sync_profile.py   (stdlib only)
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import time
import urllib.request

USER = "itsoumya-d"
HF = "itssoumyad"
AI_REPOS = [
    "HEROS-RL", "Reflexion-SWE", "GraphRAG-CodeAudit", "HEROS", "llm-control-plane",
    "Anthropic-PerfBench", "edgeinfer", "RouteLLM-Gateway", "HEROS-Firewall",
    "HEROS-Cloud-SaaS", "Mobbin-UI-Compiler", "peervault", "autopilot-fde",
    "rlvr-bias-probe",
]
HEADERS = {"User-Agent": "profile-sync", "Accept": "application/vnd.github+json"}
_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
if _token:
    HEADERS["Authorization"] = f"Bearer {_token}"


def get(url: str, retries: int = 2):
    last_exc = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            return json.loads(urllib.request.urlopen(req, timeout=30).read())
        except Exception as exc:  # rate limits, transient network
            last_exc = exc
            if attempt < retries:
                time.sleep(2 * (attempt + 1))
    raise last_exc


def prev_rows(text: str) -> dict:
    """Map repo -> previous table row / CI line from the current block."""
    out = {}
    for line in text.splitlines():
        m = re.match(r"\| \[([^\]]+)\]\(https://github\.com/itsoumya-d/", line)
        if m:
            out[("repo", m.group(1))] = line
            continue
        m = re.match(r"\[([^\]:]+): ([^\]]+)\]\(https://github\.com/itsoumya-d/[^/]+/actions\)", line)
        if m:
            out[("ci", m.group(1))] = line
    return out


def repo_table(prev: dict) -> list[str]:
    rows = []
    for name in AI_REPOS:
        try:
            d = get(f"https://api.github.com/repos/{USER}/{name}")
            desc = (d.get("description") or "").replace("|", "/").strip()
            rows.append(f"| [{name}](https://github.com/{USER}/{name}) | "
                        f"{desc or '—'} | {d.get('stargazers_count', 0)} | "
                        f"{(d.get('pushed_at') or '')[:10]} |")
        except Exception:
            if ("repo", name) in prev:  # keep last good row
                rows.append(prev[("repo", name)])
    return rows


def ci_status(prev: dict) -> list[str]:
    out = []
    for name in AI_REPOS:
        try:
            d = get(f"https://api.github.com/repos/{USER}/{name}/actions/runs?per_page=1")
            run = d["workflow_runs"][0]
            concl = run.get("conclusion") or run.get("status")
            out.append(f"[{name}: {concl}](https://github.com/{USER}/{name}/actions)")
        except Exception:
            out.append(prev.get(("ci", name),
                                f"[{name}: n/a](https://github.com/{USER}/{name}/actions)"))
    return out


def hf_block() -> list[str]:
    lines = []
    for kind, label in (("models", "Models"), ("datasets", "Datasets"), ("spaces", "Spaces")):
        try:
            items = get(f"https://huggingface.co/api/{kind}?author={HF}&limit=100")
            lines.append(f"{label} ({len(items)}): " +
                         ", ".join(f"[{x.get('id')}](https://huggingface.co/{kind}/{x.get('id')})" for x in items[:8]))
        except Exception:
            lines.append(f"{label}: (fetch failed)")
    return lines


def main() -> None:
    root = pathlib.Path(__file__).resolve().parent
    readme = root / "README.md"
    text = readme.read_text(encoding="utf-8")
    prev = prev_rows(text)

    block = ["", "### 🧪 Latest AI repos (auto-synced)", "",
             "| Repo | What it does | ★ | Last push |", "|---|---|---:|---|"]
    block += repo_table(prev)
    block += ["", "🟢/🔴 Latest CI runs (auto-synced)", ""]
    block += ci_status(prev)
    block += ["", "🤗 Hugging Face (`itssoumyad`, auto-synced)", ""]
    block += hf_block()
    auto = "\n".join(block)

    if "<!-- AUTO-START -->" in text and "<!-- AUTO-END -->" in text:
        pre, rest = text.split("<!-- AUTO-START -->", 1)
        _, post = rest.split("<!-- AUTO-END -->", 1)
        readme.write_text(
            pre + "<!-- AUTO-START -->\n" + auto + "\n<!-- AUTO-END -->" + post,
            encoding="utf-8")
        print(f"updated README ({len(text)} -> {len(readme.read_text(encoding='utf-8'))} chars), "
              f"repos kept: {len([k for k in prev if k[0] == 'repo'])}")
    else:
        readme.write_text(text + "\n<!-- AUTO-START -->\n" + auto + "\n<!-- AUTO-END -->\n",
                          encoding="utf-8")
        print("markers not found; appended AUTO block")


if __name__ == "__main__":
    main()
