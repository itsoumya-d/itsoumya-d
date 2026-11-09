"""Sync the profile README's auto-generated block.

Fetches, from public endpoints only:
  * the user's public GitHub repos (name, description, stars, last push)
  * the last CI run conclusion for each AI repo
  * the Hugging Face org's models/datasets/spaces (itssoumyad)

Then rewrites the text between
<!-- AUTO-START --> and <!-- AUTO-END --> in README.md.

Usage: python sync_profile.py   (stdlib only)
"""

from __future__ import annotations

import json
import pathlib
import urllib.request

USER = "itsoumya-d"
HF = "itssoumyad"
AI_REPOS = [
    "HEROS-RL", "Reflexion-SWE", "GraphRAG-CodeAudit", "HEROS", "llm-control-plane",
    "Anthropic-PerfBench", "edgeinfer", "RouteLLM-Gateway", "HEROS-Firewall",
    "HEROS-Cloud-SaaS", "Mobbin-UI-Compiler", "peervault", "autopilot-fde",
    "rlvr-bias-probe",
]
UA = {"User-Agent": "profile-sync", "Accept": "application/vnd.github+json"}


def get(url: str):
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read())


def repo_table() -> list[str]:
    rows = []
    for name in AI_REPOS:
        try:
            d = get(f"https://api.github.com/repos/{USER}/{name}")
        except Exception:
            continue
        desc = (d.get("description") or "").replace("|", "/").strip()
        rows.append(f"| [{name}](https://github.com/{USER}/{name}) | "
                    f"{desc or '—'} | {d.get('stargazers_count', 0)} | "
                    f"{(d.get('pushed_at') or '')[:10]} |")
    return rows


def ci_status() -> list[str]:
    out = []
    for name in AI_REPOS:
        try:
            d = get(f"https://api.github.com/repos/{USER}/{name}/actions/runs?per_page=1")
            run = d["workflow_runs"][0]
            concl = run.get("conclusion") or run.get("status")
            out.append(f"[{name}: {concl}](https://github.com/{USER}/{name}/actions)")
        except Exception:
            out.append(f"[{name}: n/a](https://github.com/{USER}/{name}/actions)")
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

    block = ["", "### 🧪 Latest AI repos (auto-synced)", "",
             "| Repo | What it does | ★ | Last push |", "|---|---|---:|---|"]
    block += repo_table()
    block += ["", "🟢/🔴 Latest CI runs (auto-synced)", ""]
    block += ci_status()
    block += ["", "🤗 Hugging Face (`itssoumyad`, auto-synced)", ""]
    block += hf_block()
    auto = "\n".join(block)

    if "<!-- AUTO-START -->" in text and "<!-- AUTO-END -->" in text:
        pre, rest = text.split("<!-- AUTO-START -->", 1)
        _, post = rest.split("<!-- AUTO-END -->", 1)
        readme.write_text(
            pre + "<!-- AUTO-START -->\n" + auto + "\n<!-- AUTO-END -->" + post,
            encoding="utf-8")
        print(f"updated README ({len(text)} -> {len(readme.read_text(encoding='utf-8'))} chars)")
    else:
        readme.write_text(text + "\n<!-- AUTO-START -->\n" + auto + "\n<!-- AUTO-END -->\n",
                          encoding="utf-8")
        print("markers not found; appended AUTO block")


if __name__ == "__main__":
    main()
