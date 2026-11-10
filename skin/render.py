"""SVG renderers for the profile skin.

Design direction (chosen with the UI UX Pro Max design data, "Swiss Modernism
2.0" + "Exaggerated Minimalism" for a personal portfolio):
  * ink + warm paper neutrals, ONE signal accent (vermilion), no gradients,
    no glow, no shadows; sharp corners; oversized tight type; hairline rules.
  * every colour pair is checked for WCAG AA (>= 4.5:1).

Pure functions: data in, SVG text out. Every asset is rendered twice (dark and
light) and the README swaps them with <picture> + prefers-color-scheme.
Animations are CSS/SMIL inside the SVG (GitHub renders them through <img>).
"""

from __future__ import annotations

import datetime as dt
import math

SANS = "'Inter Tight',Inter,'Helvetica Neue',Helvetica,'Segoe UI',Arial,sans-serif"
MONO = "'JetBrains Mono','IBM Plex Mono','SF Mono',SFMono-Regular,Consolas,Menlo,monospace"

THEMES = {
    "dark": dict(
        bg="#0C0C0B", panel="#131311", panel2="#1B1A17", line="#2B2A26", grid="#191816",
        text="#F5F1E8", body="#CFC9BC", muted="#948E82", faint="#5C574F",
        acc="#FF5722", on_acc="#0C0C0B", inv_bg="#F5F1E8", inv_fg="#0C0C0B",
        ok="#4CC38A", bad="#E5484D", warn="#F5A524",
        heat=["#1B1A17", "#3A2219", "#702C14", "#B83A12", "#FF5722"],
        ramp=["#FF5722", "#F5F1E8", "#B9B3A6", "#8A8478", "#655F56", "#47433C", "#36332E", "#2B2A26"]),
    "light": dict(
        bg="#F5F1E8", panel="#F5F1E8", panel2="#ECE6DA", line="#DCD5C6", grid="#EAE4D7",
        text="#0C0C0B", body="#3A3833", muted="#6A655B", faint="#A39D90",
        acc="#C7380A", on_acc="#FFFFFF", inv_bg="#0C0C0B", inv_fg="#F5F1E8",
        ok="#1F7A45", bad="#C8312F", warn="#A86A00",
        heat=["#E6DFD1", "#F2C8B4", "#E99A75", "#D9632F", "#C7380A"],
        ramp=["#C7380A", "#0C0C0B", "#4A4740", "#77726A", "#9D978C", "#BDB7AA", "#D3CDC1", "#E3DDD0"]),
}


# ---------------------------------------------------------------- helpers
def esc(s) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def trunc(s: str, n: int) -> str:
    s = s or ""
    return s if len(s) <= n else s[: n - 1].rstrip(" ·,-") + "…"


def wrap(s: str, width: int, max_lines: int) -> list[str]:
    words, lines, cur = (s or "").split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= width:
            cur = f"{cur} {w}" if cur else w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = trunc(lines[-1] + " …", width)
    return lines


def short_date(iso: str | None) -> str:
    if not iso:
        return "n/a"
    d = dt.date.fromisoformat(iso[:10])
    return f"{d.day} {d.strftime('%b')}"


def days_since(iso: str | None, now: dt.date) -> int:
    if not iso:
        return 9999
    return max(0, (now - dt.date.fromisoformat(iso[:10])).days)


def open_svg(w: int, h: int, label: str, css: str = "") -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{esc(label)}"><title>{esc(label)}</title>'
            f"<style>.s{{font-family:{SANS}}}.m{{font-family:{MONO}}}{css}"
            "@media (prefers-reduced-motion:reduce){*{animation:none!important}}</style>")


def text(x, y, s, *, size=14, fill="#000", cls="s", weight=400, anchor="start", ls=None,
         opacity=None, raw=False) -> str:
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls is not None else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    body = s if raw else esc(s)
    return (f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}"{a}{l}{o}>{body}</text>')


def frame(w: int, h: int, t: dict, fill: str | None = None, r: int = 8) -> str:
    return (f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="{r}" '
            f'fill="{fill or t["panel"]}" stroke="{t["line"]}"/>')


# ---------------------------------------------------------------- hero
def radar_radius(days: int, R: float) -> float:
    """Recency -> distance from centre: today sits near the core, 60+ days on the rim."""
    return 30 + (R - 30) * min(1.0, math.log1p(days) / math.log1p(60))


def hero(t: dict, ctx: dict) -> str:
    W, H = 1200, 460
    p, now = ctx["profile"], ctx["today"]
    cx, cy, R = 955, 232, 186
    css = (".rl{opacity:0;animation:cyc 12s infinite both}"
           ".rl1{animation-delay:4s}.rl2{animation-delay:8s}"
           "@keyframes cyc{0%{opacity:0}3%{opacity:1}30%{opacity:1}33%{opacity:0}100%{opacity:0}}"
           ".caret{animation:blink 1.1s steps(1) infinite}@keyframes blink{50%{opacity:0}}"
           f".sweep{{transform-origin:{cx}px {cy}px;animation:spin 9s linear infinite}}"
           "@keyframes spin{to{transform:rotate(360deg)}}"
           f".halo{{paint-order:stroke;stroke:{t['bg']};stroke-width:4px;stroke-linejoin:round}}"
           "@media (prefers-reduced-motion:reduce){.rl0{opacity:1!important}.sweep{display:none}}")
    o = [open_svg(W, H, f"{p['name']}: {p['headline']}. Live profile header.", css)]
    o.append(f'<defs><clipPath id="clip"><rect width="{W}" height="{H}" rx="8"/></clipPath></defs>')
    o.append(f'<g clip-path="url(#clip)"><rect width="{W}" height="{H}" fill="{t["bg"]}"/>')
    for gx in range(100, W, 100):  # 12-column grid hairlines
        o.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke="{t["grid"]}"/>')
    o.append("</g>")
    o.append(frame(W, H, t, fill="none"))

    # meta row
    o.append(f'<rect x="48" y="40" width="44" height="6" fill="{t["acc"]}"/>')
    o.append(f'<circle cx="53" cy="73" r="4" fill="{t["ok"]}"/>'
             f'<circle cx="53" cy="73" r="4" fill="none" stroke="{t["ok"]}" stroke-width="1.4">'
             '<animate attributeName="r" values="4;10" dur="2.2s" repeatCount="indefinite"/>'
             '<animate attributeName="opacity" values="0.9;0" dur="2.2s" repeatCount="indefinite"/></circle>')
    o.append(text(66, 77, p["open_to"].upper(), size=11, fill=t["body"], cls="m", weight=600, ls=1.2))
    o.append(text(660, 77, f"SYNCED {ctx['synced']}", size=10, fill=t["faint"], cls="m", anchor="end", ls=1.2))

    # name, set big and tight, with the accent full stop
    first, _, last = p["name"].partition(" ")
    o.append(text(42, 166, first, size=96, fill=t["text"], weight=800, ls=-4.6))
    o.append(text(42, 254, f'{esc(last)}<tspan fill="{t["acc"]}">.</tspan>', size=96, fill=t["text"],
                  weight=800, ls=-4.6, raw=True))
    o.append(text(48, 296, p["headline"], size=21, fill=t["text"], weight=650, ls=-0.3))
    o.append(text(48, 321, p["tagline"], size=13.5, fill=t["muted"], cls="m"))

    for i, line in enumerate(ctx["ticker"][:3]):
        line = trunc(line, 58)
        o.append(f'<g class="rl rl{i}">')
        o.append(text(48, 358, "❯", size=15, fill=t["acc"], cls="m", weight=700))
        o.append(text(68, 358, line, size=15, fill=t["body"], cls="m"))
        o.append(f'<rect class="caret" x="{70 + len(line) * 9.05:.1f}" y="346" width="8" height="15" fill="{t["acc"]}"/>')
        o.append("</g>")

    o.append(f'<line x1="48" y1="378" x2="660" y2="378" stroke="{t["line"]}"/>')
    for i, (val, lab) in enumerate(ctx["kpis"]):
        x = 48 + i * 156
        o.append(text(x, 416, val, size=31, fill=t["text"], weight=760, ls=-1.2))
        o.append(text(x, 438, lab.upper(), size=10, fill=t["muted"], cls="m", weight=600, ls=1.2))

    # recency radar
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{t["bg"]}" stroke="{t["line"]}"/>')
    for d, lab in ((7, "7D"), (30, "30D")):
        rr = radar_radius(d, R)
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{rr:.1f}" fill="none" stroke="{t["line"]}" stroke-dasharray="2 4"/>')
        o.append(text(cx + 5, cy - rr - 5, lab, size=9, fill=t["faint"], cls="m", weight=600, ls=1))
    o.append(f'<line x1="{cx - R}" y1="{cy}" x2="{cx + R}" y2="{cy}" stroke="{t["line"]}"/>'
             f'<line x1="{cx}" y1="{cy - R}" x2="{cx}" y2="{cy + R}" stroke="{t["line"]}"/>')
    for deg in range(0, 360, 6):
        a = math.radians(deg)
        ln = 8 if deg % 30 == 0 else 4
        x1, y1 = cx + R * math.cos(a), cy + R * math.sin(a)
        x2, y2 = cx + (R - ln) * math.cos(a), cy + (R - ln) * math.sin(a)
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{t["muted"] if ln == 8 else t["line"]}"/>')
    sweep_end = f"{cx},{cy - R + 2}"
    wedge = (f"M{cx},{cy} L{sweep_end} A{R - 2},{R - 2} 0 0,0 "
             f"{cx - (R - 2) * math.sin(math.radians(28)):.1f},{cy - (R - 2) * math.cos(math.radians(28)):.1f} Z")
    o.append(f'<g class="sweep"><path d="{wedge}" fill="{t["acc"]}" opacity="0.07"/>'
             f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - R + 2}" stroke="{t["acc"]}" stroke-width="1.2" opacity="0.7"/></g>')

    nodes = sorted(ctx["constellation"], key=lambda n: n[0].lower())
    recent = {n for n, _, _ in sorted(ctx["constellation"], key=lambda n: n[2] or "", reverse=True)[:6]}
    step = 360 / max(len(nodes), 1)
    labels: list[str] = []
    for i, (name, title, pushed) in enumerate(nodes):
        d = days_since(pushed, now)
        a = math.radians(-90 + i * step)
        r = radar_radius(d, R)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        if d <= 7:
            o.append(f'<rect x="{x - 4.5:.1f}" y="{y - 4.5:.1f}" width="9" height="9" fill="{t["acc"]}"/>')
            if d <= 2:
                o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="none" stroke="{t["acc"]}" stroke-width="1.2">'
                         f'<animate attributeName="r" values="5;15" dur="2.4s" begin="{i * 0.3:.1f}s" repeatCount="indefinite"/>'
                         f'<animate attributeName="opacity" values="0.8;0" dur="2.4s" begin="{i * 0.3:.1f}s" repeatCount="indefinite"/></circle>')
        else:
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{t["bg"]}" stroke="{t["text"]}" stroke-width="1.2" opacity="0.75"/>')
        if name in recent:
            c = math.cos(a)
            lr = max(r + 18, 74)
            lx, ly = cx + lr * c, cy + lr * math.sin(a)
            o.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="{t["muted"]}" stroke-width="0.8"/>')
            anchor = "start" if c >= 0 else "end"
            # Labels go on top of every node, with a background halo so they stay legible.
            labels.append(text(lx + (5 if c >= 0 else -5), ly + 4, trunc(title, 18), size=11.5, fill=t["text"],
                               cls="m halo", weight=600, anchor=anchor))
    o.extend(labels)
    o.append(f'<rect x="{cx - 3}" y="{cy - 3}" width="6" height="6" fill="{t["text"]}"/>')
    o.append(text(cx + 9, cy + 14, "NOW", size=9, fill=t["muted"], cls="m", weight=700, ls=1))
    o.append(text(1152, 446, "RECENCY RADAR · CLOSER TO CENTRE = PUSHED MORE RECENTLY", size=9.5,
                  fill=t["faint"], cls="m", anchor="end", ls=0.8))
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------- telemetry
def telemetry(t: dict, ctx: dict) -> str:
    W, H = 1200, 330
    o = [open_svg(W, H, "Live telemetry: activity, language mix and CI health")]
    o.append(frame(W, H, t))
    act = ctx["activity"]

    o.append(text(40, 52, "ACTIVITY", size=11, fill=t["muted"], cls="m", weight=700, ls=1.6))
    total = f"{act['total']:,}"
    o.append(text(38, 94, total, size=40, fill=t["text"], weight=780, ls=-1.6))
    o.append(text(48 + len(total) * 22, 93, act["label"], size=13, fill=t["muted"]))
    today = ctx["today"]
    start = today - dt.timedelta(days=(today.weekday() + 1) % 7 + 25 * 7)
    days = act["days"]
    vals = [v for v in days.values() if v > 0]
    peak = max(vals) if vals else 1
    cell, gap, gx, gy = 17, 4, 40, 114
    for w in range(26):
        for d in range(7):
            day = start + dt.timedelta(days=w * 7 + d)
            if day > today:
                continue
            v = days.get(day.isoformat(), 0)
            lvl = 0 if v <= 0 else min(4, 1 + int(3.999 * (v / peak) ** 0.6))
            o.append(f'<rect x="{gx + w * (cell + gap)}" y="{gy + d * (cell + gap)}" width="{cell}" height="{cell}" '
                     f'rx="2" fill="{t["heat"][lvl]}"/>')
    gend = gx + 26 * (cell + gap) - gap
    o.append(text(gx, 300, "26 WEEKS AGO", size=9.5, fill=t["faint"], cls="m", ls=0.8))
    o.append(text(gend, 300, "TODAY", size=9.5, fill=t["faint"], cls="m", anchor="end", ls=0.8))
    lx = gend - 160
    o.append(text(lx - 8, 300, "LESS", size=9.5, fill=t["faint"], cls="m", anchor="end", ls=0.8))
    for i in range(5):
        o.append(f'<rect x="{lx + i * 15}" y="291" width="11" height="11" rx="1.5" fill="{t["heat"][i]}"/>')
    o.append(text(lx + 81, 300, "MORE", size=9.5, fill=t["faint"], cls="m", ls=0.8))

    sx = 612
    for i, (val, lab) in enumerate(ctx["activity_stats"]):
        y = 142 + i * 52
        o.append(f'<line x1="{sx}" y1="{y - 30}" x2="{sx + 96}" y2="{y - 30}" stroke="{t["line"]}"/>')
        o.append(text(sx, y, val, size=23, fill=t["text"], weight=760, ls=-0.6))
        o.append(text(sx, y + 17, lab.upper(), size=9.5, fill=t["muted"], cls="m", weight=600, ls=1.1))

    o.append(f'<line x1="740" y1="36" x2="740" y2="{H - 36}" stroke="{t["line"]}"/>')

    rx0, rw = 772, 390
    o.append(text(rx0, 52, "LANGUAGE MIX", size=11, fill=t["muted"], cls="m", weight=700, ls=1.6))
    o.append(text(rx0 + rw, 52, f"{ctx['original_repos']} ORIGINAL REPOS", size=9.5, fill=t["faint"], cls="m",
                  anchor="end", ls=0.8))
    langs = ctx["languages"]
    x = rx0
    for i, (name, pct) in enumerate(langs):
        w = rw * pct / 100
        o.append(f'<rect x="{x:.1f}" y="72" width="{max(w - 2, 1):.1f}" height="14" fill="{t["ramp"][min(i, 7)]}"/>')
        x += w
    for i, (name, pct) in enumerate(langs[:6]):
        col, row = i % 2, i // 2
        lx2, ly = rx0 + col * 200, 118 + row * 28
        o.append(f'<rect x="{lx2}" y="{ly - 9}" width="9" height="9" fill="{t["ramp"][i]}" stroke="{t["line"]}" stroke-width="0.5"/>')
        o.append(text(lx2 + 18, ly, trunc(name, 14), size=13, fill=t["body"], weight=550))
        o.append(text(lx2 + 180, ly, f"{pct}%", size=12, fill=t["muted"], cls="m", anchor="end"))

    ok, total_ci, states = ctx["ci_ok"], ctx["ci_total"], ctx["ci_states"]
    o.append(text(rx0, 230, "FLAGSHIP CI", size=11, fill=t["muted"], cls="m", weight=700, ls=1.6))
    col = t["ok"] if ok == total_ci else (t["warn"] if ok >= total_ci * 0.75 else t["bad"])
    o.append(text(rx0 + rw, 230, f"{ok}/{total_ci} PASSING", size=11, fill=col, cls="m", weight=700, anchor="end", ls=0.8))
    n = max(len(states), 1)
    seg = (rw - (n - 1) * 4) / n
    for i, st in enumerate(states):
        c = {"pass": t["ok"], "fail": t["bad"], "running": t["warn"]}.get(st, t["faint"])
        o.append(f'<rect x="{rx0 + i * (seg + 4):.1f}" y="246" width="{seg:.1f}" height="20" rx="1.5" fill="{c}"/>')
    o.append(text(rx0, 300, "ONE BLOCK PER FLAGSHIP REPO · LATEST MAIN-BRANCH RUN", size=9.5, fill=t["faint"],
                  cls="m", ls=0.8))
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------- cards
def card(t: dict, c: dict) -> str:
    W, H = 580, 212
    o = [open_svg(W, H, f"{c['title']}: {c['plain']}")]
    o.append(frame(W, H, t, r=6))
    o.append(text(26, 36, c["idx"], size=11, fill=t["acc"], cls="m", weight=700, ls=1))
    o.append(text(52, 36, "/  " + c["tag"].upper(), size=10.5, fill=t["muted"], cls="m", weight=600, ls=1.2))
    status, st = c["status"], c["state"]
    dot = {"pass": t["ok"], "fail": t["bad"], "running": t["warn"], "live": t["ok"]}.get(st, t["faint"])
    sx = 554 - len(status) * 6.75
    o.append(f'<rect x="{sx - 14:.1f}" y="28" width="7" height="7" fill="{dot}"/>')
    o.append(text(554, 36, status.upper(), size=10.5, fill=t["body"], cls="m", weight=600, anchor="end", ls=0.8))
    o.append(f'<line x1="26" y1="50" x2="554" y2="50" stroke="{t["line"]}"/>')
    o.append(text(24, 90, trunc(c["title"], 28), size=30, fill=t["text"], weight=780, ls=-1.1))
    o.append(text(554, 88, "↗", size=20, fill=t["muted"], anchor="end"))
    for i, line in enumerate(wrap(c["plain"], 64, 2)):
        o.append(text(26, 119 + i * 21, line, size=15, fill=t["body"]))
    o.append(f'<rect x="26" y="{163}" width="7" height="7" fill="{t["acc"]}"/>')
    o.append(text(42, 170, trunc(c["metric"], 68), size=12.5, fill=t["text"], cls="m", weight=700))
    o.append(f'<line x1="26" y1="184" x2="554" y2="184" stroke="{t["line"]}"/>')
    o.append(text(26, 201, trunc("  ·  ".join(c["stack"]), 52), size=10.5, fill=t["muted"], cls="m"))
    o.append(text(554, 201, c["foot"], size=10.5, fill=t["muted"], cls="m", anchor="end"))
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------- section header
def section(t: dict, num: str, title: str, note: str) -> str:
    W, H = 1200, 64
    o = [open_svg(W, H, f"{num} {title}")]
    o.append(f'<rect x="0" y="27" width="22" height="5" fill="{t["acc"]}"/>')
    o.append(text(32, 36, num, size=13, fill=t["acc"], cls="m", weight=700))
    o.append(text(64, 37, title.upper(), size=16, fill=t["text"], weight=780, ls=2.4))
    end = 64 + len(title) * 13.6 + 18
    nstart = 1200 - len(note) * 7.3 - 18
    if nstart > end:
        o.append(f'<line x1="{end:.0f}" y1="31.5" x2="{nstart:.0f}" y2="31.5" stroke="{t["line"]}"/>')
    o.append(text(1200, 36, note.upper(), size=10.5, fill=t["muted"], cls="m", anchor="end", ls=1))
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------- buttons
def ask_pill(t: dict, q: str, primary: bool = False) -> str:
    W, H = 580, 64
    o = [open_svg(W, H, f"Ask: {q}")]
    if primary:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="6" fill="{t["inv_bg"]}"/>')
        fg, arrow = t["inv_fg"], t["acc"]
    else:
        o.append(frame(W, H, t, r=6))
        fg, arrow = t["text"], t["muted"]
    o.append(f'<rect x="18" y="18" width="28" height="28" fill="{t["acc"]}"/>')
    o.append(text(32, 38.5, "?", size=18, fill=t["on_acc"], weight=800, anchor="middle"))
    o.append(text(62, 39, trunc(q, 50), size=17, fill=fg, weight=640, ls=-0.2))
    o.append(text(554, 40, "→", size=20, fill=arrow, anchor="end", weight=700))
    o.append("</svg>")
    return "".join(o)


def action_pill(t: dict, label: str, kind: str) -> str:
    W, H = int(54 + len(label) * 8.6), 44
    o = [open_svg(W, H, label)]
    if kind == "primary":
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="6" fill="{t["inv_bg"]}"/>')
        fg = t["inv_fg"]
    else:
        o.append(frame(W, H, t, r=6))
        fg = t["text"]
    o.append(f'<rect x="18" y="18" width="8" height="8" fill="{t["acc"]}"/>')
    o.append(text(36, 27.5, label, size=15, fill=fg, weight=640, ls=-0.1))
    o.append("</svg>")
    return "".join(o)
