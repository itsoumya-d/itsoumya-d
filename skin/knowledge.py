"""Question answering for the README bot and the console page.

Deterministic on purpose: answers come only from profile.json and the live
data in data.json, so the bot cannot be talked into inventing claims. The same
intents (with precomputed Markdown answers) are exported to site/data.json so
the console page answers identically.
"""

from __future__ import annotations

import datetime as dt
import re

INTENT_KEYWORDS: dict[str, list[str]] = {
    "strongest": ["strongest", "best", "proud", "flagship", "impressive", "top project", "favourite",
                  "favorite", "highlight", "show me one", "standout"],
    "now": ["now", "currently", "right now", "building", "working on", "latest", "recent", "lately",
            "this week", "today"],
    "quality": ["test", "tests", "ci", "quality", "prove", "proof", "evidence", "reliab", "coverage",
                "verify", "works", "bugs", "discipline"],
    "relocation": ["relocat", "remote", "visa", "move", "location", "based", "where", "timezone",
                   "time zone", "new zealand", "nz", "singapore", "sg", "onsite", "on-site", "hybrid"],
    "agents": ["agent", "claude", "codex", "copilot", "cursor", "ai coding", "ai tools", "llm workflow",
               "prompt", "vibe"],
    "stack": ["stack", "tech", "language", "languages", "skills", "framework", "tools", "know"],
    "apps": ["app", "apps", "mobile", "flutter", "ios", "android", "app store", "play store", "shipped",
             "consumer", "users"],
    "contact": ["contact", "email", "reach", "hire", "interview", "available", "availability", "call",
                "resume", "cv", "linkedin", "salary", "notice"],
    "lens:safety": ["safety", "security", "secure", "guardrail", "firewall", "owasp", "audit", "approval"],
    "lens:platform": ["platform", "gateway", "router", "routing", "rag", "retrieval", "llm infra",
                      "infrastructure", "cost", "observability"],
    "lens:research": ["research", "rl", "reinforcement", "grpo", "training", "paper", "experiment",
                      "reflexion"],
    "lens:performance": ["performance", "fast", "kernel", "simd", "neon", "gpu", "webgpu", "wasm",
                         "browser", "edge", "latency", "p2p", "crypto"],
    "lens:backend": ["backend", "payment", "payments", "ledger", "go ", "golang", ".net", "c#", "rust",
                     "integration", "erp", "api"],
}


def fmt_date(iso: str | None) -> str:
    if not iso:
        return "n/a"
    try:
        d = dt.date.fromisoformat(iso[:10])
    except ValueError:
        return iso[:10]
    return f"{d.day} {d.strftime('%b %Y')}"


def ci_label(state: str | None) -> str:
    return {"pass": "CI passing", "fail": "CI failing", "running": "CI running",
            "none": "no CI runs yet"}.get(state or "", "CI status unknown")


def repo_url(profile: dict, name: str) -> str:
    return f"https://github.com/{profile['login']}/{name}"


def recent_repos(profile: dict, data: dict, n: int = 5) -> list[tuple[str, dict]]:
    repos = data.get("repos") or {}
    login = profile["login"]
    rows = [(k, v) for k, v in repos.items()
            if not v.get("fork") and not v.get("archived") and v.get("description")
            and k.lower() not in (login.lower(), "default-project")]
    rows.sort(key=lambda kv: kv[1].get("pushed_at") or "", reverse=True)
    return rows[:n]


def ci_summary(profile: dict, data: dict) -> tuple[int, int]:
    ci = data.get("ci") or {}
    tracked = [n for n in profile["projects"] if n in ci and ci[n].get("state") != "none"]
    ok = sum(1 for n in tracked if ci[n].get("state") == "pass")
    return ok, len(tracked)


def project_line(profile: dict, data: dict, name: str) -> str:
    p = profile["projects"][name]
    ci = (data.get("ci") or {}).get(name, {})
    pushed = fmt_date(((data.get("repos") or {}).get(name) or {}).get("pushed_at"))
    demo = f" · [live demo]({p['demo']})" if p.get("demo") else ""
    return (f"**[{p['title']}]({repo_url(profile, name)})**: {p['plain']}  \n"
            f"  `{p['metric']}` · {ci_label(ci.get('state'))} · last push {pushed}{demo}")


def app_line(app: dict) -> str:
    return (f"**{app['title']}**: {app['plain']}  \n"
            f"  [App Store]({app['app_store']}) · [Google Play]({app['play']})")


def lens_answer(profile: dict, data: dict, lens_id: str) -> str:
    lens = next(l for l in profile["lenses"] if l["id"] == lens_id)
    apps = {a["id"]: a for a in profile["apps"]}
    lines = [f"**{lens['label']}**: {lens['why']}", ""]
    for i, r in enumerate(lens["repos"], 1):
        if r.startswith("@"):
            lines.append(f"{i}. {app_line(apps[r[1:]])}")
        else:
            lines.append(f"{i}. {project_line(profile, data, r)}")
    return "\n".join(lines)


def build_intents(profile: dict, data: dict) -> list[dict]:
    """Every intent with its precomputed Markdown answer (live data baked in)."""
    ok, total = ci_summary(profile, data)
    email, linkedin = profile["email"], profile["linkedin"]
    intents: list[dict] = []

    def add(iid: str, title: str, md: str):
        intents.append({"id": iid, "title": title, "keywords": INTENT_KEYWORDS.get(iid, []), "md": md})

    strongest = [f"{i}. {project_line(profile, data, n)}" for i, n in enumerate(profile["strongest"], 1)]
    strongest.append(f"{len(strongest) + 1}. {app_line(profile['apps'][0])}")
    add("strongest", "Strongest work",
        "If you only open four things, open these:\n\n" + "\n".join(strongest))

    rec = recent_repos(profile, data)
    rec_lines = [f"- **[{k}]({v['url']})**: {v['description']} · pushed {fmt_date(v.get('pushed_at'))}"
                 for k, v in rec]
    add("now", "What I'm building now",
        "Most recent pushes, straight from the GitHub API:\n\n" + "\n".join(rec_lines))

    add("quality", "How I prove it works",
        f"Every flagship repo runs CI on each push. Right now **{ok} of {total} are green**.\n\n"
        "- Tests ship with the code: 45 in llm-control-plane (93% coverage), 95 in EdgeInfer, "
        "75 in PeerVault, 434 in Factory Monitor.\n"
        "- Benchmarks are reproducible and labelled honestly. *Synthetic*, *mock* and *pending* "
        "results are marked as such, never passed off as production numbers.\n"
        f"- Full evidence matrix: [EVIDENCE.md](https://github.com/{profile['login']}/{profile['login']}/blob/main/EVIDENCE.md)")

    add("relocation", "Location & relocation", f"{profile['relocation']}\n\n{profile['experience']}.")
    add("agents", "How I work with AI agents", profile["agents_workflow"])

    langs = data.get("languages") or []
    lang_txt = ", ".join(f"{l} {p}%" for l, p in langs[:6])
    stack_lines = [f"- **{k}**: {v}" for k, v in profile["stack"]]
    add("stack", "Tech stack",
        "\n".join(stack_lines) + (f"\n\nPrimary language across my repos (live): {lang_txt}." if lang_txt else ""))

    add("apps", "Shipped apps", "Two consumer apps, live on both stores:\n\n" +
        "\n".join(f"{i}. {app_line(a)}" for i, a in enumerate(profile["apps"], 1)))

    add("contact", "Contact",
        f"The fastest way to reach me is email: **{email}**. You can also find me on [LinkedIn]({linkedin}).\n\n"
        f"{profile['open_to']} · {profile['experience']}.")

    for lens in profile["lenses"]:
        if lens["id"] == "product":
            continue
        add(f"lens:{lens['id']}", lens["label"], lens_answer(profile, data, lens["id"]))
    return intents


def kw_hit(k: str, q: str) -> bool:
    """Word-aware keyword test (mirrored in site/index.html).

    Short keywords (<= 3 chars) must be whole words, so "ci" doesn't fire on
    "city"; longer ones match as word prefixes, so "relocat" catches
    "relocation" but "now" never fires on "know".
    """
    k = k.strip()
    lead = r"\b" if k[:1].isalnum() else ""
    tail = r"\b" if len(k) <= 3 and k[-1:].isalnum() else ""
    return re.search(lead + re.escape(k) + tail, q) is not None


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def match_repo(profile: dict, data: dict, text: str) -> str | None:
    t, low = _norm(text), text.lower()
    tracked = profile["projects"]
    # Curated projects: loose match ("heros firewall", "HerosFirewall"...).
    # Longest names first so "HEROS-Firewall" wins over "HEROS".
    for name in sorted(tracked, key=len, reverse=True):
        if _norm(name) in t or _norm(tracked[name]["title"]) in t:
            return name
    # Any other repo: only an exact, whole-word mention of its real name, so
    # generic repo names never hijack ordinary questions.
    for name in sorted(data.get("repos") or {}, key=len, reverse=True):
        if name in tracked or len(name) < 5:
            continue
        if re.search(r"(?<![\w-])" + re.escape(name.lower()) + r"(?![\w-])", low):
            return name
    return None


def repo_answer(profile: dict, data: dict, name: str) -> str:
    if name in profile["projects"]:
        return project_line(profile, data, name)
    v = (data.get("repos") or {}).get(name, {})
    return (f"**[{name}]({repo_url(profile, name)})**: {v.get('description') or 'no description yet'}  \n"
            f"  {v.get('language') or 'n/a'} · ★ {v.get('stars', 0)} · last push {fmt_date(v.get('pushed_at'))}")


def answer(profile: dict, data: dict, question: str, intents: list[dict] | None = None) -> tuple[str, str]:
    """Return (intent_id, markdown) for a free-text question."""
    intents = intents or build_intents(profile, data)
    q = f" {question.lower()} "
    repo = match_repo(profile, data, question)
    if repo:
        return "repo", repo_answer(profile, data, repo)
    best, score = None, 0
    for it in intents:
        s = sum(2 if " " in k.strip() else 1 for k in it["keywords"] if kw_hit(k, q))
        if s > score:
            best, score = it, s
    if best:
        return best["id"], best["md"]
    menu = " · ".join(f"*{x['q']}*" for x in profile["questions"])
    return "fallback", (
        f"I'm a small bot, so I couldn't match that one. Soumya gets notified of every question and "
        f"can follow up personally. Meanwhile, here's the short version:\n\n> {profile['summary']}\n\n"
        f"Things I can answer instantly: {menu}, or name any repo.")
