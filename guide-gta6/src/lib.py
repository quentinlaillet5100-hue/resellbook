# -*- coding: utf-8 -*-
"""Bibliothèque de composants : CSS, badges, encadrés, illustrations SVG originales,
carte schématique de Leonida. Toutes les illustrations sont créées pour ce guide
(aucune capture ni image de Rockstar Games)."""

import html
import urllib.parse

E = html.escape

# ----------------------------------------------------------------------------
# Couleurs par partie
# ----------------------------------------------------------------------------
PART_COLORS = {
    0: "#ff7a1a", 1: "#ff3d6e", 2: "#18d4c4", 3: "#ff7a1a", 4: "#7bd651",
    5: "#ffd23f", 6: "#e5243b", 7: "#b072ff", 8: "#38b6ff", 9: "#ff3d8b", 10: "#ffb020",
}

CSS = r"""
@page { size: 148mm 210mm; margin: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
html, body { margin: 0; padding: 0; background: #0b0a10; }
body { font-family: 'Inter', sans-serif; color: #f2eee9; font-size: 8.6pt; line-height: 1.42; }
a { color: inherit; text-decoration: none; }
.page { width: 148mm; height: 210mm; position: relative; overflow: hidden;
  background: #0d0b12; page-break-after: always; break-after: page; }
.page:last-child { page-break-after: auto; }
.bgdeco { position:absolute; inset:0; z-index:0; pointer-events:none; }
.hdr { position:absolute; top:0; left:0; right:0; height:9mm; display:flex; align-items:center;
  justify-content:space-between; padding:0 7mm; z-index:3; font-size:6.4pt; letter-spacing:.06em;
  text-transform:uppercase; background:linear-gradient(90deg, rgba(0,0,0,.55), rgba(0,0,0,.15)); }
.hdr .part { font-weight:800; }
.hdr .nav a { margin-left:2.2mm; padding:.8mm 1.8mm; border-radius:1.5mm; background:rgba(255,255,255,.09);
  font-weight:700; color:#fff; }
.ftr { position:absolute; bottom:0; left:0; right:0; height:9mm; display:flex; align-items:center;
  justify-content:space-between; padding:0 7mm; font-size:6.2pt; color:#8d8698; z-index:3; }
.ftr .num { font-family:'Inter Display'; font-weight:900; font-size:9pt; color:#fff; }
.content { position:absolute; top:11mm; bottom:10mm; left:8mm; right:8mm; z-index:2; overflow:hidden; }
h1, h2, h3, h4 { font-family:'Inter Display', 'Inter', sans-serif; margin:0; }
h2.title { font-weight:900; font-size:19pt; line-height:1.02; text-transform:uppercase; letter-spacing:-.01em; margin:1mm 0 1.2mm; }
h2.title small { display:block; font-size:7pt; letter-spacing:.18em; font-weight:800; margin-bottom:1mm; }
h3 { font-weight:800; font-size:10.5pt; margin:2.6mm 0 1.2mm; text-transform:uppercase; letter-spacing:.02em; }
h4 { font-weight:800; font-size:9pt; margin:0 0 .6mm; }
p { margin:0 0 1.6mm; }
.lead { font-size:9.2pt; color:#e8e1ea; }
.muted { color:#a9a2b3; }
.small { font-size:7.2pt; }
.tiny { font-size:6.3pt; line-height:1.35; }
ul { margin:0 0 1.6mm; padding-left:4.2mm; }
li { margin-bottom:.6mm; }
.badge { display:inline-block; font-size:5.8pt; font-weight:900; letter-spacing:.08em; padding:.45mm 1.4mm;
  border-radius:1mm; text-transform:uppercase; vertical-align:middle; white-space:nowrap; }
.b-conf { background:#1f9d55; color:#fff; }
.b-obs { background:#ff9f1a; color:#1a0f00; }
.b-nc { background:#5a5466; color:#fff; border:.25mm dashed #cfc7da; }
.b-spoil { background:#e5243b; color:#fff; }
.src { font-size:6pt; color:#9a93a6; }
.src a { color:#ffb36b; }
.card { background:linear-gradient(160deg, rgba(255,255,255,.075), rgba(255,255,255,.03));
  border:.3mm solid rgba(255,255,255,.1); border-radius:2.4mm; padding:2.4mm 2.8mm; margin-bottom:2.2mm;
  break-inside:avoid; position:relative; }
.card.accent { border-left:1.2mm solid var(--acc); }
.card .ctitle { display:flex; justify-content:space-between; align-items:flex-start; gap:2mm; }
.card .ctitle h4 { font-size:9.3pt; }
.kv { display:grid; grid-template-columns: 19mm 1fr; gap:.5mm 2mm; font-size:7.5pt; margin-top:1mm; }
.kv > b { color:#a9a2b3; font-weight:700; font-size:6.6pt; text-transform:uppercase; letter-spacing:.04em; padding-top:.3mm; }
.tip { border-radius:2.4mm; padding:2.2mm 2.8mm 2.2mm 9mm; margin:1.6mm 0 2.2mm; position:relative;
  background:rgba(24,212,196,.10); border:.3mm solid rgba(24,212,196,.45); font-size:7.8pt; break-inside:avoid; }
.tip:before { content: attr(data-ico); position:absolute; left:2.4mm; top:1.8mm; font-size:10pt; }
.tip.warn { background:rgba(229,36,59,.10); border-color:rgba(229,36,59,.5); }
.tip.gold { background:rgba(255,210,63,.09); border-color:rgba(255,210,63,.5); }
.tip b.t { display:block; text-transform:uppercase; font-size:6.8pt; letter-spacing:.08em; margin-bottom:.4mm; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:2.2mm; }
.grid3 { display:grid; grid-template-columns:1fr 1fr 1fr; gap:2mm; }
table.t { width:100%; border-collapse:collapse; font-size:7.3pt; margin:1mm 0 2mm; }
table.t th { text-align:left; font-size:6.2pt; text-transform:uppercase; letter-spacing:.06em; color:#1a0f00;
  background:var(--acc, #ff7a1a); padding:1mm 1.4mm; }
table.t td { padding:.9mm 1.4mm; border-bottom:.25mm solid rgba(255,255,255,.09); vertical-align:top; }
table.t tr:nth-child(even) td { background:rgba(255,255,255,.035); }
.emoji { font-family:'Noto Color Emoji'; }
.ill { border-radius:2.4mm; overflow:hidden; position:relative; border:.3mm solid rgba(255,255,255,.12); }
.ill .cap { position:absolute; bottom:1mm; right:1.6mm; font-size:5.2pt; color:rgba(255,255,255,.75);
  background:rgba(0,0,0,.45); padding:.2mm 1.2mm; border-radius:1mm; }
.mapbox { border-radius:2.4mm; overflow:hidden; border:.3mm solid rgba(255,255,255,.14); background:#06222d; position:relative; }
.cbrow { display:flex; align-items:flex-start; gap:1.8mm; padding:.75mm 0; border-bottom:.25mm dashed rgba(255,255,255,.1); font-size:7.5pt; }
.cb { flex:0 0 3.6mm; width:3.6mm; height:3.6mm; border:.35mm solid #ffd23f; border-radius:.7mm; margin-top:.2mm; background:rgba(255,210,63,.06); }
.cbrow .q { margin-left:auto; color:#a9a2b3; white-space:nowrap; font-size:6.8pt; }
.toc a { display:flex; align-items:baseline; gap:1.5mm; padding:.75mm 0; border-bottom:.25mm dotted rgba(255,255,255,.14); }
.toc a .dots { flex:1; }
.toc a .pg { font-family:'Inter Display'; font-weight:900; color:#ffb36b; }
.toc .pt { font-family:'Inter Display'; font-weight:900; text-transform:uppercase; font-size:8.6pt; margin-top:1.4mm; }
.toc .sub { padding-left:4mm; font-size:7.4pt; color:#d9d2de; }
.pill { display:inline-block; padding:.4mm 1.6mm; border-radius:5mm; background:rgba(255,255,255,.08); margin:0 .8mm .8mm 0; font-size:6.8pt; }
.btnrow a { display:inline-block; padding:1.2mm 2.4mm; border-radius:1.6mm; background:var(--acc,#ff7a1a); color:#140c00; font-weight:800; font-size:7pt; margin:0 1.2mm 1.2mm 0; }
.vlink { font-size:6.6pt; color:#ffb36b; font-weight:700; }
.opener h1 { font-weight:900; font-size:40pt; line-height:.9; text-transform:uppercase; letter-spacing:-.02em; }
.numbig { font-family:'Inter Display'; font-weight:900; font-size:96pt; line-height:.8; opacity:.95; }
.sec-id { scroll-margin-top: 0; }
.idx { columns:2; column-gap:5mm; font-size:7pt; }
.idx div { break-inside:avoid; padding:.35mm 0; display:flex; gap:1mm; }
.idx div .d { flex:1; border-bottom:.25mm dotted rgba(255,255,255,.18); margin-bottom:1mm; }
.idx .L { font-family:'Inter Display'; font-weight:900; color:#ffb36b; font-size:9pt; margin-top:1.2mm; }
"""

# ----------------------------------------------------------------------------
# Petits composants
# ----------------------------------------------------------------------------
def badge(status):
    s = status.upper()
    if s.startswith("CONF"):
        return '<span class="badge b-conf">✔ Confirmé</span>'
    if s.startswith("OBS"):
        return '<span class="badge b-obs">◉ Observé</span>'
    if s.startswith("SPOIL"):
        return '<span class="badge b-spoil">⚠ Spoilers</span>'
    return '<span class="badge b-nc">? Non confirmé</span>'


def tip(text, title="Astuce", kind="", ico="💡"):
    return (f'<div class="tip {kind}" data-ico="{ico}"><b class="t">{title}</b>{text}</div>'
            .replace('data-ico="', 'data-ico="'))


def yt(query, label="▶ Recherche vidéo"):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)
    return f'<a class="vlink" href="{url}">{label}</a>'


def kv(rows):
    out = '<div class="kv">'
    for k, v in rows:
        if v:
            out += f'<b>{k}</b><div>{v}</div>'
    return out + '</div>'


def card(title, body="", status=None, src="", acc="#ff7a1a", icon="", extra_cls="", right=""):
    b = badge(status) if status else ""
    ic = f'<span class="emoji" style="font-size:13pt;margin-right:1.6mm">{icon}</span>' if icon else ""
    s = f'<div class="src">Sources : {src}</div>' if src else ""
    return (f'<div class="card accent {extra_cls}" style="--acc:{acc}"><div class="ctitle"><h4>{ic}{title}</h4>'
            f'<div>{right}{b}</div></div>{body}{s}</div>')


def cbrow(label, qty="", name=""):
    q = f'<span class="q">{qty}</span>' if qty else ""
    return f'<div class="cbrow"><span class="cb" data-name="{E(name or label)}"></span><span>{label}</span>{q}</div>'


# ----------------------------------------------------------------------------
# Illustrations SVG originales
# ----------------------------------------------------------------------------
def _palms(x0, base, n, scale=1.0, color="#120a16", seed=1):
    out = ""
    import random
    r = random.Random(seed)
    for i in range(n):
        x = x0 + i * (60 * scale) + r.randint(-12, 12)
        h = (70 + r.randint(0, 40)) * scale
        lean = r.randint(-14, 14) * scale
        top = (x + lean, base - h)
        out += (f'<path d="M{x},{base} Q{x+lean*0.3},{base-h*0.5} {top[0]},{top[1]}" stroke="{color}" '
                f'stroke-width="{4*scale}" fill="none"/>')
        for a in (-1, 1):
            for k in (0, 1, 2):
                dx = a * (22 + k * 6) * scale
                dy = (6 + k * 9) * scale
                out += (f'<path d="M{top[0]},{top[1]} Q{top[0]+dx*0.6},{top[1]-10*scale} {top[0]+dx},{top[1]+dy}" '
                        f'stroke="{color}" stroke-width="{3.2*scale}" fill="none" stroke-linecap="round"/>')
    return out


def _skyline(base, w, color="#1a0f24", seed=3, maxh=120):
    import random
    r = random.Random(seed)
    x = 0
    out = ""
    while x < w:
        bw = r.randint(14, 34)
        bh = r.randint(25, max(26, int(maxh)))
        out += f'<rect x="{x}" y="{base-bh}" width="{bw}" height="{bh}" fill="{color}"/>'
        for wy in range(int(base - bh + 6), int(base - 4), 9):
            for wx in range(x + 3, x + bw - 3, 6):
                if r.random() < 0.28:
                    out += f'<rect x="{wx}" y="{wy}" width="2.4" height="3.2" fill="#ffcf7a" opacity=".75"/>'
        x += bw + r.randint(1, 5)
    return out


def scene(kind, w=400, h=170, label="Illustration originale — non issue du jeu"):
    """Scènes illustratives par type de lieu."""
    gid = f"g{kind}{w}{h}"
    sky = {
        "vice": ("#2b0f3f", "#ff3d6e", "#ffb020"),
        "keys": ("#0a3a5c", "#38b6ff", "#ffd8a0"),
        "grass": ("#13261c", "#5c8a3a", "#f3c46b"),
        "port": ("#1b1530", "#8a4b9e", "#ff9a5a"),
        "ambrosia": ("#2a1a0f", "#c0601f", "#ffd23f"),
        "kalaga": ("#0c2233", "#3a7d8c", "#f4e1b0"),
        "night": ("#05040b", "#1b1240", "#3b2b7a"),
        "cover": ("#12051d", "#c8164a", "#ff9a1a"),
        "sea": ("#032033", "#0b6e8a", "#7fe0e6"),
    }[kind]
    s = (f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" style="display:block">'
         f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{sky[0]}"/><stop offset=".62" stop-color="{sky[1]}"/>'
         f'<stop offset="1" stop-color="{sky[2]}"/></linearGradient></defs>'
         f'<rect width="{w}" height="{h}" fill="url(#{gid})"/>')
    hz = h * 0.72
    if kind in ("vice", "cover", "night"):
        s += f'<circle cx="{w*0.7}" cy="{hz-8}" r="{h*0.22}" fill="#ffcf5a" opacity=".9"/>'
        for i in range(5):
            s += f'<rect x="{w*0.7-h*0.24}" y="{hz-30+i*7}" width="{h*0.48}" height="2.2" fill="{sky[1]}"/>'
        s += _skyline(hz, w, "#1a0a26", seed=7, maxh=h * 0.55)
        s += f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#0a1a2e"/>'
        for i in range(8):
            s += f'<rect x="{w*0.58 + i*3}" y="{hz+4+i*4}" width="{60-i*6}" height="1.4" fill="#ffcf5a" opacity="{.6-i*.06}"/>'
        s += _palms(10, h, 2, 0.9 * min(h, 240) / 170, "#0a0410", seed=2)
        s += _palms(w - 70 * min(h, 240) / 170, h, 1, 1.0 * min(h, 240) / 170, "#0a0410", seed=5)
    elif kind == "keys":
        s += f'<circle cx="{w*0.25}" cy="{hz-20}" r="{h*0.13}" fill="#fff2c4" opacity=".85"/>'
        s += f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#0c79a8"/>'
        for cx, rw in ((w * .15, 60), (w * .48, 90), (w * .82, 70)):
            s += f'<ellipse cx="{cx}" cy="{hz+6}" rx="{rw}" ry="9" fill="#f1d9a2"/>'
            s += f'<ellipse cx="{cx}" cy="{hz+3}" rx="{rw*0.7}" ry="6" fill="#3d8c48"/>'
        s += f'<path d="M0,{hz-6} L{w},{hz-14}" stroke="#d8d0c0" stroke-width="3"/>'
        for i in range(0, w, 26):
            s += f'<rect x="{i}" y="{hz-14 + 8*(1-i/w)}" width="2.5" height="{14}" fill="#d8d0c0"/>'
        s += _palms(w * 0.42, hz + 6, 2, 0.45, "#173a22", seed=9)
    elif kind == "grass":
        s += f'<circle cx="{w*0.8}" cy="{hz-14}" r="{h*0.12}" fill="#ffe7a1" opacity=".8"/>'
        s += f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#20402e"/>'
        import random
        r = random.Random(4)
        for i in range(140):
            x = r.uniform(0, w)
            hh = r.uniform(8, 30)
            s += f'<path d="M{x},{hz+r.uniform(0,6)} l{r.uniform(-4,4)},{-hh}" stroke="#2f5a2c" stroke-width="1.6"/>'
        for x in (w * .12, w * .3, w * .9):
            s += f'<path d="M{x},{hz} q-3,-40 0,-60 q4,20 0,60" fill="#16301e"/>'
            s += f'<ellipse cx="{x}" cy="{hz-60}" rx="22" ry="10" fill="#16301e"/>'
        s += f'<rect y="{hz+10}" width="{w}" height="{h-hz-10}" fill="#163245"/>'
        s += (f'<path d="M{w*0.42},{hz+28} q20,-8 40,0 l18,-2 q8,2 0,5 l-18,1 q-20,6 -40,-1 z" fill="#0d1b12"/>'
              f'<circle cx="{w*0.42+44}" cy="{hz+25}" r="1.6" fill="#ffd23f"/>')
    elif kind == "port":
        s += f'<circle cx="{w*0.5}" cy="{hz}" r="{h*0.18}" fill="#ffb27a" opacity=".85"/>'
        s += f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#241a3a"/>'
        s += f'<rect x="{w*0.05}" y="{hz-8}" width="{w*0.5}" height="5" fill="#130b1f"/>'
        for i in range(10):
            s += f'<rect x="{w*0.06 + i*w*0.05}" y="{hz-8}" width="2.4" height="22" fill="#130b1f"/>'
        cx, cy, rr = w * 0.78, hz - 38, 36
        s += f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="#130b1f" stroke-width="3"/>'
        for a in range(0, 360, 30):
            import math
            s += (f'<line x1="{cx}" y1="{cy}" x2="{cx+rr*math.cos(math.radians(a))}" y2="{cy+rr*math.sin(math.radians(a))}" '
                  f'stroke="#130b1f" stroke-width="1.2"/>')
        s += f'<path d="M{cx-20},{hz} L{cx},{cy} L{cx+20},{hz}" stroke="#130b1f" stroke-width="3" fill="none"/>'
        s += _skyline(hz, w * 0.4, "#130b1f", seed=11, maxh=40).replace('<rect x="', '<rect transform="translate(0,0)" x="')
    elif kind == "ambrosia":
        s += f'<circle cx="{w*0.2}" cy="{hz-24}" r="{h*0.14}" fill="#fff0b3" opacity=".9"/>'
        s += f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#5c3b12"/>'
        for i in range(12):
            s += f'<path d="M{-20+i*40},{h} L{w*0.5},{hz}" stroke="#7a5418" stroke-width="2"/>'
        s += f'<rect x="{w*0.55}" y="{hz-50}" width="110" height="50" fill="#22140a"/>'
        for i, hh in enumerate((95, 80, 110)):
            x = w * 0.58 + i * 30
            s += f'<rect x="{x}" y="{hz-hh}" width="9" height="{hh}" fill="#22140a"/>'
            s += f'<circle cx="{x+5}" cy="{hz-hh-10}" r="9" fill="#d9c9b0" opacity=".35"/>'
            s += f'<circle cx="{x+12}" cy="{hz-hh-24}" r="12" fill="#d9c9b0" opacity=".25"/>'
    elif kind == "kalaga":
        s += f'<circle cx="{w*0.72}" cy="{hz-40}" r="{h*0.1}" fill="#fff6d8" opacity=".85"/>'
        s += f'<path d="M0,{hz} L{w*0.2},{hz-55} L{w*0.38},{hz-20} L{w*0.55},{hz-70} L{w*0.8},{hz-25} L{w},{hz-45} L{w},{hz} Z" fill="#1f4a4f"/>'
        s += f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#17343a"/>'
        s += f'<ellipse cx="{w*0.5}" cy="{hz+18}" rx="{w*0.3}" ry="10" fill="#3a8fa8" opacity=".8"/>'
        for i in range(16):
            x = i * w / 15
            hh = 26 + (i * 37) % 22
            s += f'<path d="M{x},{h} l-9,0 l9,{-hh} l9,{hh} z" fill="#0f2a24"/>'
    elif kind == "sea":
        s += f'<rect y="{h*0.25}" width="{w}" height="{h}" fill="#05536b" opacity=".7"/>'
        for i in range(7):
            s += f'<path d="M0,{h*0.25+i*14} q{w/8},-6 {w/4},0 t{w/4},0 t{w/4},0 t{w/4},0" stroke="#7fe0e6" stroke-width="1" fill="none" opacity=".35"/>'
        s += f'<path d="M{w*0.3},{h-6} l20,-30 l10,30 z M{w*0.62},{h-6} l14,-22 l12,22 z" fill="#0a2a33"/>'
    s += f'<text x="{w-6}" y="{h-5}" text-anchor="end" font-family="Inter" font-size="7" fill="#ffffff" opacity=".7">{label}</text>'
    return s + '</svg>'


# Pictogrammes de véhicules (silhouettes originales)
def vicon(kind, color="#ff7a1a", w=96, h=46):
    body = {
        "car": 'M8,34 L14,24 L30,20 L44,12 L72,12 L84,22 L92,24 L94,34 Z',
        "super": 'M4,34 L10,28 L36,22 L54,15 L72,16 L90,26 L94,34 Z',
        "muscle": 'M6,34 L8,24 L28,22 L40,13 L66,13 L76,22 L92,24 L94,34 Z',
        "suv": 'M6,34 L8,18 L20,16 L30,8 L76,8 L86,18 L92,20 L94,34 Z',
        "truck": 'M4,34 L4,8 L60,8 L60,34 Z M62,34 L62,14 L80,14 L92,24 L94,34 Z',
        "police": 'M8,34 L14,24 L30,20 L44,12 L72,12 L84,22 L92,24 L94,34 Z',
        "tank": 'M6,36 L10,24 L86,24 L92,36 Z M26,24 L32,14 L62,14 L68,24 Z M62,17 L94,15 L94,18 L62,20 Z',
    }
    if kind in body:
        extra = ""
        if kind == "police":
            extra = '<rect x="50" y="7" width="14" height="5" rx="1.5" fill="#38b6ff"/><rect x="56" y="7" width="8" height="5" rx="1.5" fill="#e5243b"/>'
        wheels = '' if kind == 'tank' else '<circle cx="26" cy="35" r="7" fill="#0d0b12" stroke="#fff" stroke-width="1.6"/><circle cx="76" cy="35" r="7" fill="#0d0b12" stroke="#fff" stroke-width="1.6"/>'
        if kind == "tank":
            wheels = ''.join(f'<circle cx="{x}" cy="37" r="4" fill="#0d0b12" stroke="#fff" stroke-width="1.2"/>' for x in range(16, 88, 12))
        g = f'<path d="{body[kind]}" fill="{color}"/>{extra}{wheels}'
        if kind in ("car", "super", "muscle", "suv", "police"):
            g += '<path d="M46,15 L70,15 L78,22 L40,22 Z" fill="#0d0b12" opacity=".55"/>'
    elif kind == "moto":
        g = (f'<circle cx="22" cy="32" r="10" fill="none" stroke="#fff" stroke-width="2.4"/>'
             f'<circle cx="74" cy="32" r="10" fill="none" stroke="#fff" stroke-width="2.4"/>'
             f'<path d="M22,32 L40,18 L62,18 L74,32 M44,18 L52,30 L62,18 M62,18 L68,10 L74,10" stroke="{color}" stroke-width="4" fill="none" stroke-linejoin="round"/>'
             f'<path d="M36,16 L58,16 L56,12 L40,12 Z" fill="{color}"/>')
    elif kind == "heli":
        g = (f'<path d="M30,28 Q30,14 48,14 L62,14 Q72,16 72,26 L72,32 L36,32 Q30,32 30,28 Z" fill="{color}"/>'
             f'<path d="M72,22 L94,18 L94,23 L72,27 Z" fill="{color}"/>'
             f'<rect x="10" y="8" width="76" height="2.2" fill="#fff"/><rect x="47" y="8" width="3" height="7" fill="#fff"/>'
             f'<path d="M34,38 L72,38 M42,32 L40,38 M62,32 L64,38" stroke="#fff" stroke-width="2"/>'
             f'<path d="M34,18 Q38,16 46,16 L46,24 L34,24 Z" fill="#0d0b12" opacity=".5"/>')
    elif kind == "plane":
        g = (f'<path d="M6,24 Q8,18 20,18 L80,18 L92,6 L96,6 L92,22 Q92,28 84,28 L18,28 Q8,28 6,24 Z" fill="{color}"/>'
             f'<path d="M40,22 L62,22 L50,40 L44,40 Z" fill="{color}" opacity=".8"/>'
             f'<path d="M12,20 L22,20 L22,24 L10,24 Z" fill="#0d0b12" opacity=".5"/>')
    elif kind == "boat":
        g = (f'<path d="M4,26 L92,26 L82,38 L14,38 Z" fill="{color}"/>'
             f'<path d="M30,26 L36,14 L64,14 L70,26 Z" fill="#fff" opacity=".85"/>'
             f'<path d="M0,42 q12,-5 24,0 t24,0 t24,0 t24,0" stroke="#38b6ff" stroke-width="2" fill="none"/>')
    elif kind == "airboat":
        g = (f'<path d="M6,30 L86,30 L80,38 L12,38 Z" fill="{color}"/>'
             f'<circle cx="70" cy="16" r="13" fill="none" stroke="#fff" stroke-width="2.4"/>'
             f'<path d="M70,4 L70,28 M58,16 L82,16" stroke="#fff" stroke-width="1.6"/>'
             f'<rect x="36" y="18" width="10" height="12" fill="{color}"/>'
             f'<path d="M0,42 q12,-5 24,0 t24,0 t24,0 t24,0" stroke="#38b6ff" stroke-width="2" fill="none"/>')
    elif kind == "jetski":
        g = (f'<path d="M10,32 L80,32 L90,26 L60,22 L44,14 L36,22 L14,24 Z" fill="{color}"/>'
             f'<path d="M0,40 q12,-5 24,0 t24,0 t24,0 t24,0" stroke="#38b6ff" stroke-width="2" fill="none"/>')
    elif kind == "bike":
        g = (f'<circle cx="24" cy="30" r="11" fill="none" stroke="#fff" stroke-width="2"/><circle cx="72" cy="30" r="11" fill="none" stroke="#fff" stroke-width="2"/>'
             f'<path d="M24,30 L40,14 L62,14 L72,30 M40,14 L48,30 L62,14 M38,10 L46,10 M62,14 L60,8 L68,8" stroke="{color}" stroke-width="3" fill="none"/>')
    else:
        g = f'<rect x="10" y="10" width="76" height="26" rx="6" fill="{color}"/>'
    return f'<svg viewBox="0 0 96 46" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">{g}</svg>'


# ----------------------------------------------------------------------------
# Carte schématique de Leonida
# ----------------------------------------------------------------------------
# Positions RELATIVES des six régions officielles (schéma non à l'échelle).
REGIONS = {
    "kalaga":   {"name": "Mount Kalaga National Park", "x": 255, "y": 78,  "rx": 70, "ry": 38, "c": "#3a9a7a"},
    "port":     {"name": "Port Gellhorn",             "x": 88,  "y": 118, "rx": 62, "ry": 34, "c": "#a05ac8"},
    "ambrosia": {"name": "Ambrosia",                  "x": 225, "y": 170, "rx": 62, "ry": 34, "c": "#d98a1f"},
    "grass":    {"name": "Grassrivers",               "x": 215, "y": 300, "rx": 58, "ry": 52, "c": "#5f9e3a"},
    "vice":     {"name": "Vice City",                 "x": 318, "y": 342, "rx": 42, "ry": 46, "c": "#ff3d6e"},
    "keys":     {"name": "Leonida Keys",              "x": 220, "y": 452, "rx": 95, "ry": 22, "c": "#38b6ff"},
}

LAND = ("M18,92 C40,60 120,52 190,46 C260,40 330,38 372,52 C384,90 380,140 372,180 "
        "C366,240 372,300 360,350 C352,388 336,410 312,416 C286,420 262,404 246,384 "
        "C226,360 196,348 172,324 C150,296 150,250 156,214 C160,186 150,170 128,160 "
        "C100,150 70,152 44,148 C24,140 12,118 18,92 Z")


def leonida_map(highlight=None, markers=(), w="100%", show_labels=True, title=True):
    hl = set(highlight or [])
    s = (f'<svg viewBox="0 0 400 500" width="{w}" xmlns="http://www.w3.org/2000/svg" style="display:block">'
         '<defs><linearGradient id="oc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#062a3a"/>'
         '<stop offset="1" stop-color="#03131d"/></linearGradient>'
         '<pattern id="gridp" width="25" height="25" patternUnits="userSpaceOnUse"><path d="M25,0 L0,0 0,25" fill="none" stroke="#0e4a5e" stroke-width=".6"/></pattern></defs>'
         '<rect width="400" height="500" fill="url(#oc)"/><rect width="400" height="500" fill="url(#gridp)" opacity=".6"/>'
         f'<path d="{LAND}" fill="#1c2a24" stroke="#3fd3c3" stroke-width="1.4" opacity=".98"/>')
    # Keys chain
    for i, (x, y, rx) in enumerate(((150, 440, 16), (182, 450, 13), (212, 456, 15), (244, 458, 12), (274, 452, 14), (300, 440, 10))):
        s += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="5" fill="#1c2a24" stroke="#3fd3c3" stroke-width="1"/>'
    s += '<path d="M150,440 Q220,470 300,440" stroke="#d8d0c0" stroke-width="1" stroke-dasharray="3 2" fill="none" opacity=".6"/>'
    for key, r in REGIONS.items():
        on = key in hl
        op = ".55" if on else (".22" if not hl else ".10")
        s += (f'<ellipse cx="{r["x"]}" cy="{r["y"]}" rx="{r["rx"]}" ry="{r["ry"]}" fill="{r["c"]}" opacity="{op}" '
              f'stroke="{r["c"]}" stroke-width="{2.4 if on else 1}" stroke-dasharray="{"" if on else "4 3"}"/>')
        if show_labels:
            fs = 12 if on else 10
            s += (f'<text x="{r["x"]}" y="{r["y"]+4}" text-anchor="middle" font-family="Inter Display" font-weight="900" '
                  f'font-size="{fs}" fill="#fff" opacity="{1 if (on or not hl) else .55}" style="text-transform:uppercase">{E(r["name"])}</text>')
    # Ocean labels
    s += ('<text x="40" y="300" font-family="Inter" font-style="italic" font-size="10" fill="#6fc6d6" opacity=".7">Golfe</text>'
          '<text x="370" y="250" font-family="Inter" font-style="italic" font-size="10" fill="#6fc6d6" opacity=".7" text-anchor="end" transform="rotate(90 370 250)">Océan</text>')
    # Compass
    s += ('<g transform="translate(360,450)"><circle r="17" fill="#0b0a10" stroke="#3fd3c3"/>'
          '<path d="M0,-13 L5,0 L0,13 L-5,0 Z" fill="#ffd23f"/><text y="-19" text-anchor="middle" font-size="8" fill="#fff" font-family="Inter" font-weight="800">N</text></g>')
    for m in markers:
        reg = REGIONS[m[0]]
        dx, dy = (m[3] if len(m) > 3 else (0, -reg["ry"] * 0.35))
        x, y = reg["x"] + dx, reg["y"] + dy
        col = m[2] if len(m) > 2 else "#ffd23f"
        s += (f'<g transform="translate({x},{y})"><path d="M0,0 C-9,-11 -9,-22 0,-22 C9,-22 9,-11 0,0 Z" fill="{col}" stroke="#0b0a10" stroke-width="1.4"/>'
              f'<text y="-12" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="9" fill="#0b0a10">{E(str(m[1]))}</text></g>')
    if title:
        s += ('<text x="12" y="490" font-family="Inter" font-size="8.5" fill="#9fd9e0">Schéma de repérage — non à l\'échelle. Positions relatives des 6 régions officielles.</text>')
    return s + '</svg>'
