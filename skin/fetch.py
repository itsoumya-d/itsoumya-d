"""Live data for the profile skin (stdlib only).

Every section is fetched independently. If one fails (rate limit, outage), the
last good value from the previous ``skin/data.json`` is kept, so the README
never degrades to blanks.

Uses GITHUB_TOKEN when present (Actions provides one): higher rate limit and
the real contribution calendar via GraphQL. Without a token it falls back to
the public events feed (last ~90 days).

Set SKIN_CACHE_DIR to cache raw responses on disk while iterating locally.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import pathlib
import time
import urllib.error
import urllib.request

TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
CACHE = os.environ.get("SKIN_CACHE_DIR")
UA = "profile-skin/1.0 (+https://github.com/itsoumya-d/itsoumya-d)"


def _cache_path(url: str, body: bytes | None) -> pathlib.Path | None:
    if not CACHE:
        return None
    key = hashlib.sha1(url.encode() + (body or b"")).hexdigest()[:16]
    p = pathlib.Path(CACHE)
    p.mkdir(parents=True, exist_ok=True)
    return p / f"{key}.json"


def http_json(url: str, body: dict | None = None, retries: int = 2):
    raw = json.dumps(body).encode() if body is not None else None
    cp = _cache_path(url, raw)
    if cp and cp.exists():
        return json.loads(cp.read_text(encoding="utf-8"))
    headers = {"User-Agent": UA, "Accept": "application/vnd.github+json"}
    if TOKEN and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {TOKEN}"
    if raw is not None:
        headers["Content-Type"] = "application/json"
    last = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, data=raw, headers=headers)
            out = json.loads(urllib.request.urlopen(req, timeout=30).read())
            if cp:
                cp.write_text(json.dumps(out), encoding="utf-8")
            return out
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code in (401, 403, 404, 422):
                break
        except Exception as exc:  # transient network
            last = exc
        if attempt < retries:
            time.sleep(2 * (attempt + 1))
    raise last  # type: ignore[misc]


def url_ok(url: str) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
        return urllib.request.urlopen(req, timeout=20).status == 200
    except Exception:
        return False


# --------------------------------------------------------------------------
def fetch_user(login: str) -> dict:
    d = http_json(f"https://api.github.com/users/{login}")
    keep = ("login", "name", "bio", "location", "public_repos", "followers",
            "created_at", "html_url", "avatar_url")
    return {k: d.get(k) for k in keep}


def fetch_repos(login: str) -> dict:
    repos = {}
    for page in range(1, 6):
        batch = http_json(f"https://api.github.com/users/{login}/repos"
                          f"?per_page=100&page={page}&type=owner&sort=pushed")
        for r in batch:
            repos[r["name"]] = {
                "description": (r.get("description") or "").strip(),
                "language": r.get("language"),
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "pushed_at": r.get("pushed_at"),
                "url": r.get("html_url"),
                "default_branch": r.get("default_branch") or "main",
                "fork": bool(r.get("fork")),
                "archived": bool(r.get("archived")),
                "size": r.get("size", 0),
                "homepage": r.get("homepage") or "",
            }
        if len(batch) < 100:
            break
    return repos


def fetch_ci(login: str, names: list[str], repos: dict) -> dict:
    out = {}
    for name in names:
        if name not in repos:
            continue
        branch = repos[name].get("default_branch", "main")
        d = http_json(f"https://api.github.com/repos/{login}/{name}/actions/runs"
                      f"?per_page=1&branch={branch}&exclude_pull_requests=true")
        runs = d.get("workflow_runs") or []
        if not runs:
            out[name] = {"state": "none"}
            continue
        run = runs[0]
        concl = run.get("conclusion") or run.get("status") or "unknown"
        state = {"success": "pass", "failure": "fail", "cancelled": "fail",
                 "timed_out": "fail", "startup_failure": "fail"}.get(concl, "running")
        out[name] = {"state": state, "conclusion": concl,
                     "at": (run.get("updated_at") or "")[:10], "url": run.get("html_url")}
    return out


def fetch_activity(login: str) -> dict:
    """Daily activity counts. Real calendar with a token, events feed otherwise."""
    if TOKEN:
        q = ("query($login:String!){user(login:$login){contributionsCollection{"
             "contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}")
        d = http_json("https://api.github.com/graphql", {"query": q, "variables": {"login": login}})
        cal = d["data"]["user"]["contributionsCollection"]["contributionCalendar"]
        days = {c["date"]: c["contributionCount"]
                for w in cal["weeks"] for c in w["contributionDays"]}
        return {"source": "calendar", "days": days, "total": cal["totalContributions"],
                "label": "contributions in the last year"}
    days: dict[str, int] = {}
    for page in range(1, 4):
        batch = http_json(f"https://api.github.com/users/{login}/events/public?per_page=100&page={page}")
        for e in batch:
            day = (e.get("created_at") or "")[:10]
            if not day:
                continue
            if e.get("type") == "PushEvent":
                n = (e.get("payload") or {}).get("distinct_size") or (e.get("payload") or {}).get("size") or 1
            elif e.get("type") in ("PullRequestEvent", "IssuesEvent", "CreateEvent",
                                   "PullRequestReviewEvent", "ReleaseEvent"):
                n = 1
            else:
                continue
            days[day] = days.get(day, 0) + int(n)
        if len(batch) < 100:
            break
    return {"source": "events", "days": days, "total": sum(days.values()),
            "label": "public commits & PRs, last 90 days"}


def fetch_hf(author: str) -> dict:
    out = {}
    for kind in ("models", "datasets", "spaces"):
        items = http_json(f"https://huggingface.co/api/{kind}?author={author}&limit=100")
        out[kind] = sorted(x.get("id") for x in items if x.get("id"))
    return out


def count_answered(login: str) -> int:
    """Questions the README bot has answered (issues labelled 'answered')."""
    n = 0
    for page in range(1, 11):
        batch = http_json(f"https://api.github.com/repos/{login}/{login}/issues"
                          f"?labels=answered&state=all&per_page=100&page={page}")
        n += len(batch)
        if len(batch) < 100:
            break
    return n


# --------------------------------------------------------------------------
def collect(profile: dict, prev: dict) -> tuple[dict, list[str]]:
    """Fetch everything; fall back to ``prev`` per section. Returns (data, warnings)."""
    login, warnings = profile["login"], []
    data: dict = {}

    def section(key, fn):
        try:
            data[key] = fn()
        except Exception as exc:
            warnings.append(f"{key}: {exc!s:.120}")
            if key in prev:
                data[key] = prev[key]

    section("user", lambda: fetch_user(login))
    section("repos", lambda: fetch_repos(login))
    tracked = list(profile["projects"].keys())
    repos = data.get("repos", {})
    section("ci", lambda: fetch_ci(login, tracked, repos))
    # Keep last-known CI per repo if this run lost some.
    for name, v in (prev.get("ci") or {}).items():
        data.setdefault("ci", {}).setdefault(name, v)
    section("activity", lambda: fetch_activity(login))
    section("hf", lambda: fetch_hf(profile["hf"]))
    data["pages"] = url_ok(f"https://{login}.github.io/{login}/")
    return data, warnings


def today() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
