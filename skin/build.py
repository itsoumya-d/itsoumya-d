#!/usr/bin/env python3
"""Build the living profile README ("Mission Control" skin).

    python skin/build.py            # fetch live data, render everything
    python skin/build.py --offline  # re-render from skin/data.json only

Outputs (all generated, never edit by hand):
    README.md, assets/skin/*.svg, skin/data.json, site/data.json

Words live in skin/profile.json; design lives in skin/render.py. When the live
data is unchanged, the output is byte-identical, so the hourly workflow only
commits when something real happened.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import sys
import urllib.parse
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import fetch  # noqa: E402
import knowledge  # noqa: E402
import render  # noqa: E402

ASSETS = ROOT / "assets" / "skin"
REL = "assets/skin"


def load_json(p: pathlib.Path, default):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return default


def languages(repos: dict) -> tuple[list[tuple[str, int]], int]:
    orig = [v for v in repos.values() if not v.get("fork") and v.get("language")]
    c = Counter(v["language"] for v in orig)
    total = sum(c.values()) or 1
    top = c.most_common(7)
    rows = [(k, round(100 * n / total)) for k, n in top]
    other = 100 - sum(p for _, p in rows)
    if other > 0:
        rows.append(("Other", other))
    return rows, len([v for v in repos.values() if not v.get("fork")])


def activity_stats(act: dict, today: dt.date) -> list[tuple[str, str]]:
    days = act.get("days") or {}
    active = sum(1 for v in days.values() if v > 0)
    best = max(days.values()) if days else 0
    streak, d = 0, today
    if days.get(d.isoformat(), 0) == 0:
        d -= dt.timedelta(days=1)  # today may not have started yet
    while days.get(d.isoformat(), 0) > 0:
        streak += 1
        d -= dt.timedelta(days=1)
    return [(str(active), "active days"), (str(best), "best day"), (f"{streak}d", "current streak")]


def make_ctx(profile: dict, live: dict, synced: str, answered: int) -> dict:
    today = dt.date.fromisoformat(synced)
    repos = live.get("repos") or {}
    langs, original = languages(repos)
    ok, total = knowledge.ci_summary(profile, live)
    ci = live.get("ci") or {}
    tracked = [n for n in profile["projects"] if n in repos]
    by_push = sorted(tracked, key=lambda n: repos[n].get("pushed_at") or "", reverse=True)
    recent = knowledge.recent_repos(profile, live, 1)
    hf = live.get("hf") or {}
    user = live.get("user") or {}
    ticker = []
    if recent:
        k, v = recent[0]
        ticker.append(f"shipping {k} · pushed {render.short_date(v.get('pushed_at'))}")
    ticker.append(f"{ok}/{total} flagship systems passing CI right now")
    ticker.append(f"{len(profile['apps'])} apps live on the App Store & Google Play")
    return {
        "profile": profile,
        "today": today,
        "synced": synced,
        "ticker": ticker,
        "kpis": [
            (str(user.get("public_repos") or len(repos)), "public repos"),
            (f"{ok}/{total}", "CI green"),
            (str(len(profile["apps"])), "apps shipped"),
            (str(len(hf.get("spaces") or [])), "live demos"),
        ],
        "constellation": [(n, profile["projects"][n]["title"], repos[n].get("pushed_at")) for n in by_push],
        "activity": {**(live.get("activity") or {"days": {}, "total": 0, "label": "activity"})},
        "activity_stats": activity_stats(live.get("activity") or {}, today),
        "languages": langs,
        "original_repos": original,
        "ci_ok": ok,
        "ci_total": total,
        "ci_states": [ci.get(n, {}).get("state", "none") for n in by_push],
        "answered": answered,
    }


def card_data(profile: dict, live: dict, name: str) -> dict:
    p = profile["projects"][name]
    lens = next((l["label"] for l in profile["lenses"] if l["id"] == p["lens"]), p["lens"])
    repo = (live.get("repos") or {}).get(name, {})
    st = (live.get("ci") or {}).get(name, {}).get("state", "none")
    status = {"pass": "CI passing", "fail": "CI failing", "running": "CI running"}.get(st, "no CI yet")
    stars = repo.get("stars", 0)
    foot = f"pushed {render.short_date(repo.get('pushed_at'))}" + (f"  ★ {stars}" if stars else "")
    idx = f"{list(profile['projects']).index(name) + 1:02d}"
    return {"title": p["title"], "plain": p["plain"], "metric": p["metric"], "stack": p["stack"],
            "tag": lens, "status": status, "state": st, "foot": foot, "idx": idx}


def app_card_data(app: dict, i: int) -> dict:
    return {"title": app["title"], "plain": app["plain"], "metric": "Live on the App Store & Google Play",
            "stack": app["stack"], "tag": "Shipped consumer app", "status": "live", "state": "live",
            "foot": "iOS · Android", "idx": f"A{i}"}


# ---------------------------------------------------------------- README
def pic(name: str, alt: str, width: str = "100%") -> str:
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{REL}/{name}-dark.svg">'
            f'<img src="{REL}/{name}-light.svg" alt="{render.esc(alt)}" width="{width}"></picture>')


def link_pic(href: str, name: str, alt: str, width: str) -> str:
    return f'<a href="{render.esc(href)}">{pic(name, alt, width)}</a>'


def card_rows(items: list[tuple[str, str, str]]) -> str:
    """items: (href, asset name, alt). Two per row."""
    rows = []
    for i in range(0, len(items), 2):
        rows.append("<p>" + " ".join(link_pic(h, n, a, "49%") for h, n, a in items[i:i + 2]) + "</p>")
    return "\n".join(rows)


def ask_url(profile: dict, q: str) -> str:
    login = profile["login"]
    title = urllib.parse.quote(f"ask: {q}" if q else "ask: ")
    return f"https://github.com/{login}/{login}/issues/new?template=ask.yml&title={title}"


def readme(profile: dict, live: dict, ctx: dict) -> str:
    login, p = profile["login"], profile
    console = f"https://{login}.github.io/{login}/"
    has_console = bool(live.get("pages"))
    repo_href = lambda n: f"https://github.com/{login}/{n}"  # noqa: E731
    apps = {a["id"]: a for a in p["apps"]}

    def proj_item(n):
        return (repo_href(n), f"card-{n}", f"{p['projects'][n]['title']}: {p['projects'][n]['plain']}")

    def lens_item(r):
        if r.startswith("@"):
            a = apps[r[1:]]
            return (a["app_store"], f"card-app-{a['id']}", f"{a['title']}: {a['plain']}")
        return proj_item(r)

    out = ["<!-- Generated by skin/build.py: edit skin/profile.json (words) or skin/render.py (design), "
           "not this file. Rebuilt hourly by .github/workflows/skin.yml. -->", "",
           '<div align="center">', "",
           link_pic(console if has_console else f"https://github.com/{login}", "hero",
                    f"{p['name']}, {p['headline']}: live profile header", "100%"), ""]
    actions = [(f"mailto:{p['email']}", "pill-email", "Email me"),
               (p["linkedin"], "pill-linkedin", "LinkedIn")]
    if has_console:
        actions.insert(0, (console, "pill-console", "Open the interactive console"))
    actions.append(("PROJECTS.md", "pill-log", "Full engineering log"))
    out.append(" ".join(f'<a href="{render.esc(h)}"><picture><source media="(prefers-color-scheme: dark)" '
                        f'srcset="{REL}/{n}-dark.svg"><img src="{REL}/{n}-light.svg" alt="{render.esc(a)}" '
                        f'height="44"></picture></a>' for h, n, a in actions))
    out += ["", "</div>", "", f"> {p['summary']}", "", "<br>", ""]

    # 01 telemetry
    out += [pic("sec-01", "01 Live telemetry"), "", pic("telemetry", "Live activity, language mix and CI health"),
            "", "<br>", ""]

    # 02 lenses
    out += [pic("sec-02", "02 Hiring for a specific role? Pick a lens"), ""]
    icons = {"platform": "🧠", "safety": "🛡️", "research": "🔬", "performance": "⚡", "product": "📱",
             "backend": "🧱"}
    for lens in p["lenses"]:
        out += [f"<details><summary><b>{icons.get(lens['id'], '▸')}&nbsp; {render.esc(lens['label'])}</b>"
                f"&nbsp;&nbsp;<sub>{render.esc(lens['why'])}</sub></summary>", "<br>", "",
                card_rows([lens_item(r) for r in lens["repos"]]), "", "</details>", ""]
    out += ["<br>", ""]

    # 03 flagship
    featured = [n for n in p["featured"] if n in p["projects"]]
    rest = [n for n in p["projects"] if n not in featured]
    out += [pic("sec-03", "03 Flagship systems"), "", card_rows([proj_item(n) for n in featured]), "",
            f"<details><summary><b>Show {len(rest)} more tracked systems</b></summary><br>", "",
            card_rows([proj_item(n) for n in rest]), "", "</details>", "", "<br>", ""]

    # 04 apps
    out += [pic("sec-04", "04 Shipped to real users"), "",
            card_rows([(a["app_store"], f"card-app-{a['id']}", f"{a['title']}: {a['plain']}") for a in p["apps"]]), "",
            '<p align="center">' + " &nbsp;·&nbsp; ".join(
                f"<b>{a['title']}</b>: <a href=\"{a['app_store']}\">App Store</a> · "
                f"<a href=\"{a['play']}\">Google Play</a> · <a href=\"{a['case_study']}\">case study</a>"
                for a in p["apps"]) + "</p>", "", "<br>", ""]

    # 05 ask
    out += [pic("sec-05", "05 Ask my README"), "",
            "Click a question and GitHub opens an issue with it already filled in. Submit it, and a bot "
            "built into this repo replies in the thread, usually within a minute, using **live** data "
            "from my repos. I get notified too and often follow up personally.", "",
            card_rows([(ask_url(p, x["q"]), f"ask-{x['intent']}", x["q"]) for x in p["questions"]]), "",
            '<p align="center">' + link_pic(ask_url(p, ""), "ask-custom", "Ask anything else", "60%") + "</p>", "",
            "<p align=\"center\"><sub>💬 " + (
                f"<b>{ctx['answered']}</b> question{'s' if ctx['answered'] != 1 else ''} answered so far"
                if ctx["answered"] else "Be the first to ask") +
            " · you can also name any repo, e.g. <i>ask: tell me about PeerVault</i></sub></p>",
            "", "<br>", ""]

    # 06 deep dive
    hf = live.get("hf") or {}
    out += [pic("sec-06", "06 Deep dive & credentials"), "",
            "| Go deeper | What you'll find |", "|:--|:--|",
            "| 📚 **[Full engineering log](PROJECTS.md)** | Every project with its exact test counts, "
            "metrics and honest limits |",
            "| 🧾 **[Evidence matrix](EVIDENCE.md)** · **[Release audit](AUDIT.md)** | What was measured, how, "
            "and what is explicitly not claimed |",
            "| 🧪 **Case studies** | " + " · ".join(
                f"[{t}](case-studies/{f})" for t, f in (("CTrackAI", "ctrackai-engineering.md"),
                                                         ("Preeo", "preeo-architecture.md"),
                                                         ("FieldLens", "fieldlens-offline-engine.md"))) + " |",
            f"| 🤗 **[Hugging Face](https://huggingface.co/{p['hf']})** | {len(hf.get('spaces') or [])} live "
            f"Spaces · {len(hf.get('datasets') or [])} datasets · [portfolio hub]"
            f"(https://huggingface.co/spaces/{p['hf']}/portfolio) |"]
    for title, url in p["credentials"]:
        out.append(f"| 🎓 {render.esc(title)} | [verify credential]({url}) |")
    out += ["", "<br>", "",
            f'<p align="center"><sub>This README rebuilds itself every hour from live GitHub and Hugging Face '
            f"data · last change {ctx['synced']} · engine: <a href=\"skin/build.py\">skin/build.py</a>"
            f"</sub></p>", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- site data
def site_data(profile: dict, live: dict, ctx: dict, intents: list[dict]) -> dict:
    repos = live.get("repos") or {}
    ci = live.get("ci") or {}
    projects = []
    for n, pr in profile["projects"].items():
        r = repos.get(n, {})
        projects.append({"name": n, **pr, "url": f"https://github.com/{profile['login']}/{n}",
                         "pushed_at": r.get("pushed_at"), "stars": r.get("stars", 0),
                         "language": r.get("language"), "ci": ci.get(n, {}).get("state", "none")})
    recent = [{"name": k, "description": v["description"], "pushed_at": v.get("pushed_at"), "url": v["url"]}
              for k, v in knowledge.recent_repos(profile, live, 6)]
    keep = ("login", "hf", "name", "headline", "tagline", "roles", "summary", "location", "open_to",
            "experience", "email", "linkedin", "stack", "apps", "lenses", "questions", "credentials", "featured")
    return {
        "synced": ctx["synced"],
        "profile": {k: profile[k] for k in keep},
        "kpis": ctx["kpis"],
        "ticker": ctx["ticker"],
        "projects": projects,
        "recent": recent,
        "languages": ctx["languages"],
        "ci": {"ok": ctx["ci_ok"], "total": ctx["ci_total"]},
        "activity": {"total": ctx["activity"].get("total", 0), "label": ctx["activity"].get("label", ""),
                     "stats": ctx["activity_stats"]},
        "hf": live.get("hf") or {},
        "answered": ctx["answered"],
        "intents": [{k: it[k] for k in ("id", "title", "keywords", "md")} for it in intents],
        "repo_names": sorted(k for k, v in repos.items() if not v.get("fork")),
    }


def theme_css() -> str:
    """The console page's colour tokens, generated from render.THEMES (one palette, two surfaces)."""
    keys = ("bg", "panel", "panel2", "line", "grid", "text", "body", "muted", "faint", "acc", "on_acc",
            "inv_bg", "inv_fg", "ok", "bad", "warn")

    def block(t: dict) -> str:
        return ("".join(f"--{k.replace('_', '-')}:{t[k]};" for k in keys)
                + "".join(f"--ramp{i}:{c};" for i, c in enumerate(t["ramp"])))

    d, l = render.THEMES["dark"], render.THEMES["light"]
    return ("/* Generated by skin/build.py from skin/render.py THEMES. Do not edit. */\n"
            f":root{{{block(d)}color-scheme:dark}}\n"
            f":root[data-theme=\"light\"]{{{block(l)}color-scheme:light}}\n")


# ---------------------------------------------------------------- main
def write_if_changed(path: pathlib.Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="re-render from skin/data.json, no network")
    args = ap.parse_args()

    profile = load_json(HERE / "profile.json", None)
    prev = load_json(HERE / "data.json", {})
    prev_live = prev.get("live") or {}

    if args.offline:
        live, warnings = prev_live, []
        answered = prev.get("answered", 0)
    else:
        live, warnings = fetch.collect(profile, prev_live)
        try:
            answered = fetch.count_answered(profile["login"])
        except Exception as exc:
            warnings.append(f"answered: {exc!s:.100}")
            answered = prev.get("answered", 0)

    canon = json.dumps({"live": live, "answered": answered, "profile": profile}, sort_keys=True)
    digest = hashlib.sha256(canon.encode()).hexdigest()[:16]
    synced = prev.get("synced") if prev.get("hash") == digest and prev.get("synced") else fetch.today()

    ctx = make_ctx(profile, live, synced, answered)
    intents = knowledge.build_intents(profile, {**live, "languages": ctx["languages"]})

    files: dict[pathlib.Path, str] = {}
    for theme, t in render.THEMES.items():
        files[ASSETS / f"hero-{theme}.svg"] = render.hero(t, ctx)
        files[ASSETS / f"telemetry-{theme}.svg"] = render.telemetry(t, ctx)
        for n in profile["projects"]:
            files[ASSETS / f"card-{n}-{theme}.svg"] = render.card(t, card_data(profile, live, n))
        for i, a in enumerate(profile["apps"], 1):
            files[ASSETS / f"card-app-{a['id']}-{theme}.svg"] = render.card(t, app_card_data(a, i))
        sections = [
            ("01", "Live telemetry", "rebuilt hourly by GitHub Actions"),
            ("02", "Hiring for…? pick a lens", "click a role to expand"),
            ("03", "Flagship systems", f"{ctx['ci_ok']}/{ctx['ci_total']} passing CI · live"),
            ("04", "Shipped to real users", "iOS · Android"),
            ("05", "Ask my README", "a bot answers in about a minute"),
            ("06", "Deep dive & credentials", "evidence over adjectives"),
        ]
        for num, title, note in sections:
            files[ASSETS / f"sec-{num}-{theme}.svg"] = render.section(t, num, title, note)
        for x in profile["questions"]:
            files[ASSETS / f"ask-{x['intent']}-{theme}.svg"] = render.ask_pill(t, x["q"])
        files[ASSETS / f"ask-custom-{theme}.svg"] = render.ask_pill(t, "Ask anything else", primary=True)
        files[ASSETS / f"pill-console-{theme}.svg"] = render.action_pill(t, "Open the interactive console", "primary")
        files[ASSETS / f"pill-email-{theme}.svg"] = render.action_pill(t, "Email me", "primary")
        files[ASSETS / f"pill-linkedin-{theme}.svg"] = render.action_pill(t, "LinkedIn", "plain")
        files[ASSETS / f"pill-log-{theme}.svg"] = render.action_pill(t, "Full engineering log", "plain")

    files[ROOT / "README.md"] = readme(profile, live, ctx)
    files[HERE / "data.json"] = json.dumps({"hash": digest, "synced": synced, "answered": answered,
                                            "live": live}, indent=1, sort_keys=True) + "\n"
    files[ROOT / "site" / "data.json"] = json.dumps(site_data(profile, live, ctx, intents), indent=1) + "\n"
    files[ROOT / "site" / "theme.css"] = theme_css()

    # Drop stale generated assets (e.g. a project removed from profile.json).
    if ASSETS.exists():
        for f in ASSETS.glob("*.svg"):
            if f not in files:
                f.unlink()
    changed = [str(p.relative_to(ROOT)) for p, c in files.items() if write_if_changed(p, c)]
    for w in warnings:
        print(f"warning: {w}")
    print(f"synced={synced} hash={digest} files={len(files)} changed={len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
