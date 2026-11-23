# -*- coding: utf-8 -*-
"""Partie 9 (checklist), Partie 10 (best-of), dernières découvertes, index,
sources, sommaire et 4e de couverture."""

import unicodedata
from lib import badge, tip, card, cbrow, scene, E, PART_COLORS
from sources import s, SOURCES, NATURE_FR, VERIF_DATE
from content_a import opener
from content_b import CHAPTERS, SF, RARE, ANIMALS
from content_c import EGGS, COLL

REQ = [
    ("Histoire principale terminée", "1", "OBS", (27,)),
    ("Tâches optionnelles", "100", "OBS", (27,)),
    ("Opérations de gangs (opérations illégales)", "39 / 39", "OBS", (27, 37)),
    ("Bank jobs", "22 / 22", "OBS", (27,)),
    ("Payday loan jobs", "7 / 7", "OBS", (27,)),
    ("Coffres-forts", "8 / 8", "OBS", (28,)),
    ("Recel : stupéfiants", "100 000 $", "OBS", (28,)),
    ("Recel : bijoux", "100 000 $", "OBS", (28,)),
    ("Recel : billets marqués", "250 000 $", "OBS", (28,)),
    ("Recel : véhicules", "200 000 $", "OBS", (28,)),
    ("Smash 'N' Grabs", "34 / 35", "OBS", (29,)),
    ("Stick Ups (braquages de magasins)", "50 / 91", "OBS", (29,)),
    ("Cocaine Flamingos", "100 / 125", "OBS", (30,)),
    ("Paniers de basket", "90 / 100", "OBS", (30,)),
    ("Scans WAiNK", "100", "OBS", (27,)),
    ("Découvertes sous-marines", "33", "OBS", (27,)),
    ("Animaux étudiés", "100 / 255", "OBS", (27,)),
    ("Véhicules scannés", "200 / 277", "OBS", (27,)),
    ("Séries de cartes complètes", "15 / 18", "OBS", (34,)),
    ("Spots de méditation", "15 / 18", "OBS", (35,)),
    ("Défis de course en or", "10/13 ? 30 ? 42 ?", "NC", (28, 31, 32)),
    ("Cascades", "300 (sur 397 ?)", "NC", (33,)),
    ("Contre-la-montre en drone", "?", "NC", (29,)),
    ("Styles découverts", "?", "NC", (29,)),
]


def part9(book):
    a = book.anchor("check", "Partie 9 — Checklist 100 %", 1)
    rows = "".join(cbrow(f'{n} {badge(st) if st == "NC" else ""}', q, f"req_{i}") for i, (n, q, st, _) in enumerate(REQ))
    body = f'''{a}<h2 class="title"><small style="color:#ff3d8b">PARTIE 9 · CHECKLIST INTERACTIVE</small>Objectif 100 %</h2>
<p class="small">Cochez les cases au fur et à mesure (puis enregistrez le PDF). Les seuils viennent des guides publiés depuis la sortie {s(27,28,29,30)}. Ceux marqués {badge("NC")} sont contradictoires d'une source à l'autre : <b>vérifiez dans le menu Progression du jeu</b>, qui fait foi {s(33)}.</p>
<div class="grid2" style="gap:0 4mm">{rows}</div>'''
    book.add(9, body)

    ch = "".join(cbrow(c.split(" — ")[0] + (f' <span class="tiny muted">{c.split(" — ")[1]}</span>' if " — " in c else ""), r, f"ch_{i}") for i, (c, r, _) in enumerate(CHAPTERS))
    sf = "".join(cbrow(f"<b>{n}</b> · {q}", f"Ch. {c}", f"sf_{i}") for i, (c, n, q, _, _) in enumerate(SF))
    a = book.anchor("check-histoire", "Checklist : histoire et quêtes", 2)
    body = f'''{a}<h2 class="title"><small style="color:#ff3d8b">CHECKLIST</small>Histoire &amp; quêtes</h2>
<p>{badge("SPOIL")}</p>
<h3>Chapitres</h3>{ch}
<h3>Strangers &amp; Freaks</h3>{sf}
<h3>Missions clés</h3>
{cbrow("« Buck Me » : application BuckMe débloquée", "Ch. 1", "k1")}
{cbrow("« Island Dreams » : découvertes sous-marines débloquées", "Ch. 1", "k2")}
{cbrow("« That's Where The Money Is… » : coffres-forts débloqués", "Ch. 4", "k3")}
{cbrow("Trophée Pest Control : une opération par gang", "9 gangs", "k4")}'''
    book.add(9, body)

    a = book.anchor("check-secrets", "Checklist : secrets, véhicules, lieux", 2)
    ee = "".join(cbrow(e["n"], f'#{e["num"]}', f"ee_{i}") for i, e in enumerate(EGGS))
    rv = "".join(cbrow(r[0], "", f"rv_{i}") for i, r in enumerate(RARE))
    regs = "".join(cbrow(n, "", f"rg_{i}") for i, n in enumerate(["Vice City", "Leonida Keys", "Grassrivers", "Port Gellhorn", "Ambrosia", "Mount Kalaga National Park"]))
    body = f'''{a}<h2 class="title"><small style="color:#ff3d8b">CHECKLIST</small>Secrets &amp; trouvailles</h2>
<div class="grid2" style="gap:0 4mm"><div><h3>Easter Eggs</h3>{ee}<h3>Régions visitées</h3>{regs}</div>
<div><h3>Véhicules rares</h3>{rv}
<h3>Garages</h3>{cbrow("Mitchell Auto Center", "4 000 $", "g1")}{cbrow("Persistence Road", "", "g2")}{cbrow("Vela Rota Drive", "", "g3")}{cbrow("Atlantic Court", "", "g4")}{cbrow("Tous les garages achetés (Little Boxes)", "8", "g5")}</div></div>'''
    book.add(9, body)

    a = book.anchor("check-faune", "Checklist : faune et collectibles", 2)
    an = "".join(cbrow(f'<span class="emoji">{x[1]}</span> {x[0]}', "", f"an_{i}") for i, x in enumerate(ANIMALS))
    co = "".join(cbrow(f'<span class="emoji">{c[1]}</span> {c[0]}', c[3], f"co_{i}") for i, c in enumerate(COLL[:8]))
    body = f'''{a}<h2 class="title"><small style="color:#ff3d8b">CHECKLIST</small>Faune &amp; collectibles</h2>
<div class="grid2" style="gap:0 4mm"><div><h3>Espèces observées</h3>{an}</div>
<div><h3>Catégories terminées</h3>{co}
<h3>Pêche</h3>{cbrow("Canne récupérée (Key Lento)", "", "f1")}{cbrow("Défi de Cal réussi (Gambit Bay)", "", "f2")}
<h3>Codes</h3>{cbrow("Générique de fin atteint : codes débloqués", "", "c1")}</div></div>'''
    book.add(9, body)


def part10(book):
    opener(book, 10, "Le meilleur", "Nos classements, uniquement à partir d'éléments suffisamment documentés. Les listes seront allongées au fil des découvertes vérifiées.",
           "cover", ["Les 20 meilleures astuces", "Les 10 découvertes les plus marquantes", "Les 12 lieux incontournables",
                     "Les véhicules les plus rares", "Les secrets les plus difficiles"], "p10")
    tips = [
        "Récupérez la canne à pêche gratuite sur le ponton de Key Lento.", "Utilisez les haltères de la terrasse de Jason dès le début.",
        "Débloquez BuckMe et déposez votre liquide.", "Ne cherchez pas à accumuler beaucoup d'argent au chapitre 1.",
        "Scannez chaque voiture avec WAiNK avant de la voler.", "Moses ne prend que les voitures sans traceur.",
        "Chapitre 3 : le Pay 'n' Spray rachète les voitures à traceur standard.", "Après un délit, changez de tenue et de véhicule.",
        "Contre un hélicoptère, passez dans un tunnel.", "Quittez la zone de recherche affichée sur la carte.",
        "Gardez votre Focus pour les combats difficiles.", "Pêchez en mode Focus (L3 + R3).",
        "Entraînez Jason ET Lucia.", "Survolez les icônes d'opérations illégales pour voir le butin.",
        "Faites la chaîne de Yago au plus tôt (limitée dans le temps).", "Videz votre stock chez Donnie avant la fin du chapitre 1.",
        "Faites « Island Dreams » pour débloquer les épaves.", "Préparez une fuite avant chaque coffre-fort (4 étoiles).",
        "Étudiez 100 animaux aux jumelles, sans chasser.", "Gardez une sauvegarde propre avant d'utiliser un code de triche.",
    ]
    tl = "".join(f'<div style="display:flex;gap:1.6mm;padding:.55mm 0;border-bottom:.25mm dotted rgba(255,255,255,.12)"><b style="color:#ffb020;font-family:Inter Display;width:5mm">{i+1:02d}</b><span class="small">{t}</span></div>' for i, t in enumerate(tips))
    a = book.anchor("p10-astuces", "Top 20 astuces", 2)
    book.add(10, f'''{a}<h2 class="title"><small style="color:#ffb020">CLASSEMENT</small>Top 20 astuces</h2>
<p class="tiny muted">Vous attendiez un « Top 50 » : à ce jour, 20 astuces sont assez documentées pour être publiées. Le classement sera complété dans les mises à jour. Les détails et les sources sont dans les Parties 1, 3, 4, 5 et 7.</p>{tl}''')

    a = book.anchor("p10-decouvertes", "Top découvertes, lieux, raretés et secrets difficiles", 2)
    disc = [e["n"] for e in EGGS][:7] + ["La Pegassi Infernus du commissariat de Crosstown", "La Pegassi Charred Torus dorée de Casanova Island", "Le défi de pêche de Cal à Gambit Bay"]
    lieux = ["Ocean Beach", "Downtown Vice City", "Jack of Hearts", "Key Lento", "Gambit Bay", "Cottonmouth Lake", "Gellhorn International Raceway",
             "Port de croisière (VC Port)", "Little Cuba", "Stockyard", "Mount Kalaga National Park", "Ambrosia"]
    rares = ["Pegassi Charred Torus (dorée)", "Pegassi Infernus", "Pegassi Tempesta", "Pegassi Vitello", "Annis Drifter Elegy", "Emperor Sultan (récompense)"]
    hard = [("L'OVNI du comté de Kelly", "De nuit, après 2 h, avec plusieurs essais"), ("Le « Cool Dog » en jet-ski", "Rencontre aléatoire"),
            ("Le Skunk Ape", "Plusieurs passages dans les marais"), ("L'œuf de l'antenne", "Escalade et emplacement contesté")]
    ol = lambda L, col: "".join(f'<div class="small" style="padding:.4mm 0"><b style="color:{col}">{i+1}.</b> {x}</div>' for i, x in enumerate(L))
    body = f'''{a}<h2 class="title"><small style="color:#ffb020">LE MEILLEUR DE LEONIDA</small>Nos sélections</h2>
<div class="grid2">
<div class="card accent" style="--acc:#e5243b"><h4>🔎 Top 10 découvertes</h4>{ol(disc, "#ff5a6e")}</div>
<div class="card accent" style="--acc:#18d4c4"><h4>📍 12 lieux incontournables</h4>{ol(lieux, "#18d4c4")}</div>
<div class="card accent" style="--acc:#ffd23f"><h4>🏎️ Les véhicules les plus rares</h4>{ol(rares, "#ffd23f")}</div>
<div class="card accent" style="--acc:#b072ff"><h4>🧩 Les secrets les plus difficiles</h4>{"".join(f'<div class="small" style="padding:.4mm 0"><b style="color:#b072ff">{i+1}.</b> {n} <span class="tiny muted">· {w}</span></div>' for i, (n, w) in enumerate(hard))}</div>
</div>
<p class="tiny muted">Vous attendiez un « Top 25 découvertes » et un « Top 20 lieux » : ces sélections seront étendues quand assez de découvertes auront été vérifiées. Ces classements sont éditoriaux. Les statuts de fiabilité de chaque élément figurent dans sa fiche.</p>'''
    book.add(10, body)


def latest(book):
    a = book.anchor("maj", "Dernières découvertes et mises à jour", 1)
    body = f'''{a}<h2 class="title"><small style="color:#18d4c4">RUBRIQUE ÉVOLUTIVE</small>Dernières découvertes</h2>
<p class="small">Cette rubrique est mise à jour à chaque nouvelle version du guide. Chaque ajout porte sa date et son statut.</p>
<table class="t" style="--acc:#18d4c4"><tr><th>Version</th><th>Date</th><th>Contenu</th></tr>
<tr><td><b>1.0</b></td><td>23/11/2026</td><td>Édition de lancement (J+4) : 10 parties, 9 Easter Eggs, 11 véhicules rares, 22 fiches faune, checklist 100 % interactive, environ 100 sources.</td></tr></table>
<h3>Prévu dans les prochaines versions</h3>
<ul class="small">
<li>Fiches détaillées mission par mission (objectif, déroulement, récompenses, éléments à ne pas manquer).</li>
<li>Emplacements des collectibles, région par région (cartes, flamants, scans WAiNK…).</li>
<li>Vitesses mesurées et classements par catégorie de véhicules.</li>
<li>Événements aléatoires recensés et défis spéciaux.</li>
<li>Vérification ou abandon des rumeurs de la Partie 6.</li>
<li>Version PC, si elle est annoncée.</li>
</ul>
{tip("Les informations marquées {o} ou {n} seront revues en priorité, au fur et à mesure que la communauté les recoupe.".replace("{o}", badge("OBS")).replace("{n}", badge("NC")), "Notre engagement", "gold", "🔄")}'''
    book.add(0, body)


def _fold(t):
    t = t.replace("&amp;", "&").replace("« ", "").replace("'", "'")
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn").upper()


def index_pages(book):
    seen = {}
    for term, cat, pg in book.index:
        key = (term, cat)
        seen.setdefault(key, set()).add(pg)
    items = sorted(seen.items(), key=lambda kv: _fold(kv[0][0]))
    per = 62
    chunks = [items[i:i + per] for i in range(0, len(items), per)]
    for ci, ch in enumerate(chunks):
        a = book.anchor("index", "Index alphabétique", 1) if ci == 0 else ""
        out, last = "", None
        for (term, cat), pgs in ch:
            L = _fold(term)[:1]
            if L != last:
                out += f'<div class="L">{L}</div>'
                last = L
            links = ", ".join(f'<a href="#pg-{p}" style="color:#ffb36b;font-weight:800">{p}</a>' for p in sorted(pgs))
            out += f'<div><span>{term} <span class="muted" style="font-size:5.6pt">· {cat}</span></span><span class="d"></span><span>{links}</span></div>'
        head = (f'<h2 class="title"><small style="color:#ffb36b">VÉHICULES · ANIMAUX · LIEUX · PERSONNAGES · SECRETS</small>Index A–Z</h2>' if ci == 0
                else '<h2 class="title" style="font-size:14pt"><small style="color:#ffb36b">INDEX (SUITE)</small></h2>')
        book.add(0, f'{a}{head}<div class="idx">{out}</div>')


def sources_pages(book):
    per = 17
    for ci in range(0, len(SOURCES), per):
        a = book.anchor("sources", "Sources et vérifications", 1) if ci == 0 else ""
        rows = ""
        for sid, ed, title, url, nat in SOURCES[ci:ci + per]:
            rows += (f'<div id="src-{sid}" style="display:flex;gap:1.6mm;padding:.55mm 0;border-bottom:.25mm dotted rgba(255,255,255,.12);break-inside:avoid">'
                     f'<b style="color:#ffb36b;width:6mm;font-family:Inter Display">[{sid}]</b><div style="flex:1" class="tiny">'
                     f'<b>{E(ed)}</b> — {E(title)} <span class="muted">· {NATURE_FR[nat]} · vérifié le {VERIF_DATE}</span><br>'
                     f'<a href="{E(url)}" style="color:#7fd6e0;word-break:break-all">{E(url)}</a></div></div>')
        head = (f'<h2 class="title"><small style="color:#ffb36b">TRAÇABILITÉ</small>Sources</h2>'
                f'<p class="tiny muted">Vérification : recherche web, le {VERIF_DATE}. Nature : Officiel (Rockstar / Take-Two), Presse, Guide communautaire, Wiki de fans. '
                f'Le statut de chaque information est indiqué dans le corps du guide. Une source citée n\'implique pas que nous en validions tout le contenu.</p>' if ci == 0
                else '<h2 class="title" style="font-size:14pt"><small style="color:#ffb36b">SOURCES (SUITE)</small></h2>')
        book.add(0, f'{a}{head}{rows}')


def back_cover(book):
    body = (f'<div style="position:absolute;inset:0">{scene("vice", 560, 794, label="")}</div>'
            '<div style="position:absolute;inset:0;background:linear-gradient(180deg,#0b0a10 0%, rgba(11,10,16,.85) 50%, rgba(11,10,16,.4) 100%)"></div>'
            '<div style="position:absolute;top:22mm;left:12mm;right:12mm">'
            '<div style="font-family:Inter Display;font-weight:900;font-size:26pt;line-height:.95">LE GUIDE QUI VOUS FAIT GAGNER DES DIZAINES D\'HEURES.</div>'
            '<ul style="margin-top:5mm;font-size:8.4pt;line-height:1.6">'
            '<li>Les 6 régions de Leonida et les lieux à ne pas manquer</li><li>Véhicules rares : où et comment les obtenir</li>'
            '<li>Une encyclopédie de la faune avec carte des habitats</li><li>Easter Eggs localisés, rumeurs séparées</li>'
            '<li>Checklist 100 % cochable</li><li>Environ 100 sources citées et datées</li></ul>'
            '<div style="margin-top:5mm;display:flex;gap:2mm"><span class="badge b-conf">✔ Confirmé</span><span class="badge b-obs">◉ Observé</span><span class="badge b-nc">? Non confirmé</span></div>'
            '<p style="margin-top:6mm;font-size:6.4pt;color:#b9b0c4">Guide indépendant et non officiel. Il n\'est ni édité, ni approuvé, ni affilié à Rockstar Games ou Take-Two Interactive. '
            'Toutes les illustrations sont originales. Grand Theft Auto et les marques associées appartiennent à leurs propriétaires respectifs. Version 1.0 du 23/11/2026.</p></div>')
    book.add(0, body, raw=True)


def toc(book, slots):
    entries = book.toc
    per = (len(entries) + len(slots) - 1) // len(slots)
    for si, slot in enumerate(slots):
        chunk = entries[si * per:(si + 1) * per]
        out = ""
        for lvl, label, aid in chunk:
            pg = book.anchor_page.get(aid, "")
            if lvl == 1:
                out += f'<a class="pt" href="#{aid}"><span>{E(label)}</span><span class="dots"></span><span class="pg">{pg}</span></a>'
            else:
                out += f'<a class="sub" href="#{aid}"><span>{E(label)}</span><span class="dots"></span><span class="pg">{pg}</span></a>'
        head = ('<span id="sommaire"></span><h2 class="title"><small style="color:#ff7a1a">NAVIGATION RAPIDE · TOUT EST CLIQUABLE</small>Sommaire</h2>' if si == 0
                else '<h2 class="title" style="font-size:14pt"><small style="color:#ff7a1a">SOMMAIRE (SUITE)</small></h2>')
        book.add(0, f'{head}<div class="toc">{out}</div>', slot=slot)
