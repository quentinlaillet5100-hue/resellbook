# -*- coding: utf-8 -*-
"""Parties 6 (Easter Eggs), 7 (astuces), 8 (collectibles)."""

from lib import badge, tip, card, kv, scene, leonida_map, yt, E
from sources import s
from content_a import opener

DIFF = {1: "●○○ Facile", 2: "●●○ Moyen", 3: "●●● Difficile"}

EGGS = [
    dict(id="ee-skunk", n="Le Skunk Ape (Bigfoot)", emo="🦍", reg="grass", sc="grass", diff=2, st="OBS",
         where="Marais autour de <b>Cottonmouth Lake</b> (comté de Mariana). Certains guides citent <b>Gullet Marsh</b>.",
         how="Explorez les marais. La chaîne de quêtes de <b>Kirk</b> (chapitre 1) est consacrée à sa traque.",
         cond="Disponible dès l'exploration libre selon un guide. Plusieurs passages peuvent être nécessaires.",
         what="Le Skunk Ape est une créature du folklore de Floride, ici dans la tradition des Bigfoot cachés de la série.",
         src=(50, 48, 40), q="GTA 6 Skunk Ape location"),
    dict(id="ee-ufo", n="L'enlèvement par un OVNI", emo="🛸", reg="port", off=(40, 8), sc="night", diff=3, st="OBS",
         where="Route rurale du <b>comté de Kelly</b>, près du <b>Starlet Motel</b>, à l'est de Port Gellhorn.",
         how="Repérez une <b>voiture abandonnée qui brille</b> au bord de la route : elle déclenche l'enlèvement.",
         cond="<b>De nuit</b>, après environ <b>2 h du matin</b> (heure du jeu) selon un guide. Un autre le décrit comme un spoiler de l'histoire.",
         what="La série multiplie les clins d'œil aux extraterrestres depuis San Andreas.",
         src=(50, 48, 51), q="GTA 6 UFO abduction Kelly County"),
    dict(id="ee-egg", n="Le véritable « œuf de Pâques »", emo="🥚", reg="vice", off=(-6, 30), sc="vice", diff=2, st="OBS",
         where="Un nid avec un œuf peint au sommet d'une <b>antenne radio</b>. Les sources ne s'accordent pas : la plus haute tour de Vice City, ou un mât au nord de Hamlet (South Vice-Dale).",
         how="Grimpez au sommet, puis <b>jetez l'œuf</b> dans le vide.",
         cond="Aucune condition signalée.",
         what="L'œuf tombe sur le pare-brise d'une voiture et déclenche une courte cinématique comique.",
         src=(48, 50, 52), q="GTA 6 easter egg radio tower nest"),
    dict(id="ee-dexter", n="L'appartement de Dexter", emo="🔪", reg="vice", off=(14, 22), sc="vice", diff=1, st="OBS",
         where="Vice City. La plupart des guides le placent sur <b>Washington Island</b> (nord-est de la ville). D'autres citent la marina de Bay Harbor ou Vice Beach.",
         how="Rendez-vous à l'adresse et observez la façade et l'intérieur.",
         cond="Aucune condition signalée.",
         what="Une référence à l'appartement de la série TV <i>Dexter</i>, qui se déroule à Miami.",
         src=(50, 48, 52), q="GTA 6 Dexter apartment easter egg"),
    dict(id="ee-belville", n="La maison de San Andreas (Belville)", emo="🏠", reg=None, sc="port", diff=1, st="OBS",
         where="<b>Belville</b>, au sud du comté de Leonard.",
         how="Cherchez la maison de banlieue qui correspond à la mystérieuse photo.",
         cond="Aucune condition signalée.",
         what="Elle correspondrait à la photo énigmatique cachée dans <i>GTA San Andreas Definitive Edition</i> (2021), longtemps vue comme un teasing de GTA VI.",
         src=(50, 48), q="GTA 6 Belville San Andreas house photo"),
    dict(id="ee-dog", n="Le « Cool Dog » en jet-ski", emo="🐕", reg="keys", off=(-40, -2), sc="keys", diff=3, st="OBS",
         where="En pleine mer, par exemple à <b>Gambit Bay</b> (Leonida Keys).",
         how="Si vous <b>entendez aboyer</b>, attendez : un chien à lunettes arrive en jet-ski et peut vous emmener faire un tour.",
         cond="<b>Rencontre aléatoire</b> : rien ne garantit son apparition.",
         what="Un des secrets les plus partagés de la semaine de lancement.",
         src=(52, 64, 48), q="GTA 6 dog jet ski"),
    dict(id="ee-hat", n="Le chapeau d'Arthur Morgan", emo="🤠", reg="port", off=(-14, 0), sc="port", diff=2, st="OBS",
         where="Un <b>vide-grenier</b> dans le sud de Port Gellhorn.",
         how="Repérez le chapeau de cowboy parmi les objets du stand.",
         cond="Aucune condition signalée.",
         what="Un clin d'œil au héros de <i>Red Dead Redemption 2</i>.",
         src=(53, 48), q="GTA 6 Arthur Morgan hat yard sale"),
    dict(id="ee-ff", n="Hommage à Paul Walker (Fast &amp; Furious)", emo="🏎️", reg=None, sc="night", diff=2, st="OBS",
         where="<b>Emplacement non documenté</b> de façon fiable.",
         how="Une voiture évoquant l'Eclipse de <i>Fast &amp; Furious</i> est signalée.",
         cond="—",
         what="La presse signale aussi un hommage au pilote de NASCAR <b>Kyle Busch</b>.",
         src=(48, 52, 56), q="GTA 6 Paul Walker tribute car"),
    dict(id="ee-novel", n="Le roman western de Jacob's Tavern", emo="📕", reg=None, sc="kalaga", diff=1, st="OBS",
         where="<b>Jacob's Tavern</b>, à Millport.",
         how="Repérez le livre dans la taverne.",
         cond="—",
         what="Un roman western signalé par GameSpot, probablement un clin d'œil à l'univers western de Rockstar.",
         src=(55,), q="GTA 6 Jacob's Tavern Millport western novel"),
]

RUMORS = [
    ("Le crabe géant de Gullet Marsh", "Signalé par des joueurs, sans confirmation.", (48,)),
    ("Le PNJ inspiré de Tom Cruise dans <i>Collateral</i>", "Signalé, sans confirmation.", (48,)),
    ("Une discussion de bar sur le « Mount Chiliad »", "Signalée, sans confirmation.", (48,)),
    ("Les listes de « codes téléphone » façon GTA V", "Ce sont des codes de GTA V recyclés : aucun numéro de triche n'est connu.", (69,)),
]


def part6(book):
    opener(book, 6, "Easter Eggs & secrets", "Les références, les mystères et les clins d'œil repérés depuis le lancement, avec leur position, les conditions et la difficulté. Les rumeurs sont séparées en fin de partie.",
           "night", ["Carte des secrets", "9 fiches détaillées", "Les rumeurs à vérifier"], "p6")

    a = book.anchor("p6-carte", "Carte des secrets", 2)
    mk = []
    for i, e in enumerate(EGGS):
        e["num"] = i + 1
        if e["reg"]:
            mk.append((e["reg"], str(i + 1), "#e5243b", e.get("off", (0, -10))))
    leg = "".join(f'<a href="#{e["id"]}" style="display:flex;gap:1.4mm;padding:.55mm 0;border-bottom:.25mm dotted rgba(255,255,255,.15)">'
                  f'<b style="color:#ff5a6e;width:4mm">{e["num"]}</b><span class="emoji">{e["emo"]}</span><span class="small" style="flex:1">{e["n"]}</span>'
                  f'<span class="tiny muted">{"" if e["reg"] else "hors carte"}</span></a>' for e in EGGS)
    body = f'''{a}<h2 class="title"><small style="color:#e5243b">VUE D'ENSEMBLE</small>Carte des secrets</h2>
<div class="grid2" style="grid-template-columns:1fr 1fr"><div class="mapbox">{leonida_map(markers=mk)}</div><div>{leg}</div></div>
<p class="tiny muted" style="margin-top:1.4mm">« Hors carte » : la région n'est pas précisée par les sources. Seul le repère textuel est donné. Les épingles situent la région, pas le point exact. Pour un positionnement exact, utilisez aussi la carte interactive « Easter Eggs » de GTABase {s(54)}.</p>
{tip("Les guides publiés quelques jours après la sortie se corrigent encore. Quand deux sources se contredisent, nous donnons les deux emplacements.", "Fiabilité", "", "🔍")}'''
    book.add(6, body)

    for i in range(0, len(EGGS), 2):
        pair = EGGS[i:i + 2]
        body = ""
        for e in pair:
            book.ix(e["n"].replace("&amp;", "&"), "Easter Egg")
            book.anchor(e["id"], e["n"].replace("&amp;", "&") if i == 0 and e is pair[0] else None, 3)
            mini = (f'<div class="mapbox" style="width:30mm;flex:0 0 30mm">{leonida_map(highlight=[e["reg"]], markers=[(e["reg"], str(e["num"]), "#e5243b", e.get("off", (0, -10)))], show_labels=False, title=False)}</div>'
                    if e["reg"] else '<div class="mapbox" style="width:30mm;flex:0 0 30mm;display:flex;align-items:center;text-align:center;font-size:6pt;color:#9fd9e0;padding:1.4mm">Région non précisée : voir le repère</div>')
            body += (f'<span id="{e["id"]}"></span><div class="card accent" style="--acc:#e5243b;padding:0;overflow:hidden;margin-bottom:2.4mm">'
                     f'<div class="ill" style="height:22mm;border:none;border-radius:0">{scene(e["sc"], 420, 80)}'
                     f'<div style="position:absolute;left:3mm;top:2mm;display:flex;gap:2mm;align-items:center"><span class="emoji" style="font-size:18pt">{e["emo"]}</span>'
                     f'<span style="font-family:Inter Display;font-weight:900;font-size:11.5pt;text-shadow:0 1px 3px #000">#{e["num"]} · {e["n"]}</span></div></div>'
                     f'<div style="display:flex;gap:2.4mm;padding:2.2mm 2.8mm"><div style="flex:1">'
                     f'<div style="display:flex;gap:2mm;margin-bottom:.8mm">{badge(e["st"])}<span class="badge" style="background:#2a2333">{DIFF[e["diff"]]}</span></div>'
                     f'{kv([("Où", e["where"]), ("Comment", e["how"]), ("Conditions", e["cond"]), ("Explication", e["what"])])}'
                     f'<div class="src" style="margin-top:.8mm">Sources : {s(*e["src"])} · {yt(e["q"])}</div></div>{mini}</div></div>')
        book.add(6, body)

    a = book.anchor("p6-rumeurs", "Rumeurs à vérifier", 2)
    rows = "".join(f'<div class="card" style="border-style:dashed"><div class="ctitle"><h4>{n}</h4>{badge("NC")}</div><p class="small">{d}</p><div class="src">Signalé par : {s(*sr)}</div></div>'
                   for n, d, sr in RUMORS)
    body = f'''{a}<h2 class="title"><small style="color:#8d8698">ZONE NON CONFIRMÉE</small>Rumeurs &amp; théories</h2>
<p class="small">Ces éléments circulent mais <b>n'ont pas été vérifiés</b>. Ils ne sont pas comptés dans les checklists.</p>
{rows}
{tip("Méfiez-vous des listes de « 50 Easter Eggs » publiées le jour de la sortie : beaucoup reprennent des théories d'avant la sortie. Une découverte sérieuse donne un lieu précis et une vidéo.", "Esprit critique", "warn", "🧠")}'''
    book.add(6, body)


# ---------------------------------------------------------------------------
# PARTIE 7 — ASTUCES
# ---------------------------------------------------------------------------
def part7(book):
    opener(book, 7, "Astuces & techniques", "Argent, conduite, combat, exploration et police : les techniques documentées, distinguées des simples hypothèses. Avec les codes de triche connus.",
           "night", ["Gagner de l'argent", "Conduite, vol et revente", "Combat et Focus", "Exploration", "Codes de triche"], "p7")

    a = book.anchor("p7-astuces", "Astuces vérifiées et hypothèses", 2)
    ver = [
        ("💰", "Déposez votre argent liquide sur <b>BuckMe</b> avant chaque mission risquée.", s(87, 23)),
        ("📡", "Avant de voler une voiture pour Moses, <b>scannez-la avec WAiNK</b> : sans traceur, sinon il la refuse.", s(87, 38)),
        ("🛠️", "À partir du chapitre 3, revendez les voitures à <b>traceur standard</b> dans un Pay 'n' Spray.", s(38)),
        ("👕", "Après un délit, <b>changez de tenue et de véhicule</b> : le Heat retient vos signes distinctifs.", s(16, 19)),
        ("🚇", "Contre un hélicoptère, <b>passez dans un tunnel</b> ou sous un abri.", s(19)),
        ("🗺️", "<b>Sortez de la zone de recherche</b> affichée sur la carte pour mettre fin à la poursuite.", s(15, 19)),
        ("🎯", "Gardez la jauge de <b>Focus</b> pour les combats difficiles : elle ralentit le temps.", s(20)),
        ("🎣", "Utilisez le Focus en pêche (<b>L3 + R3</b>) pour repérer les bancs de poissons.", s(65)),
        ("🏋️", "Entraînez <b>Jason et Lucia</b> séparément : leurs statistiques ne sont pas partagées.", s(20)),
        ("🏴", "Survolez une icône d'<b>opération illégale</b> sur la carte pour voir le butin avant d'y aller.", s(37)),
        ("⏳", "Faites la chaîne de courses de <b>Yago</b> sans tarder : elle est signalée comme limitée dans le temps.", s(41)),
        ("🧳", "Revendez vos stupéfiants à <b>Donnie</b> avant la fin du chapitre 1 : ensuite, il n'est plus disponible.", s(38)),
        ("🌊", "Terminez « Island Dreams » pour débloquer les <b>découvertes sous-marines</b> (33 au total).", s(35)),
        ("🏦", "Les <b>coffres-forts</b> donnent 4 étoiles : préparez votre fuite (véhicule de rechange, tenue).", s(39)),
        ("🐾", "Étudiez les animaux aux <b>jumelles</b> : 100 entrées du journal suffisent pour le 100 %, sans chasser.", s(27, 59)),
    ]
    hyp = [
        ("Les opérations illégales attireraient moins de Heat que les braquages de magasins.", s(39)),
        ("La pêche ferait progresser la statistique Focus.", s(59)),
        ("Les dépôts BuckMe ne se feraient qu'aux distributeurs.", s(87)),
        ("L'argent liquide et le solde BuckMe seraient perdus à la fin du chapitre 1.", s(25)),
    ]
    vr = "".join(f'<div style="display:flex;gap:1.8mm;padding:.75mm 0;border-bottom:.25mm dashed rgba(255,255,255,.1)"><span class="emoji">{e}</span><span class="small" style="flex:1">{t}</span><span class="src">{sr}</span></div>' for e, t, sr in ver)
    hr = "".join(f'<li class="small">{t} <span class="src">{sr}</span></li>' for t, sr in hyp)
    body = f'''{a}<h2 class="title"><small style="color:#b072ff">TECHNIQUES</small>Les astuces utiles</h2>
<p>{badge("OBS")} <span class="small">Astuces documentées par plusieurs sources ou par un guide détaillé</span></p>
{vr}
<div class="card" style="border-style:dashed;margin-top:2mm"><div class="ctitle"><h4>Hypothèses à tester</h4>{badge("NC")}</div><ul>{hr}</ul></div>'''
    book.add(7, body)

    a = book.anchor("p7-triche", "Codes de triche", 2)
    arrows = "↑ → ↓ ← ↑ ← ↓ →"
    body = f'''{a}<h2 class="title"><small style="color:#b072ff">CHEAT CODES</small>Codes de triche</h2>
<div class="grid2">
{card("Comment saisir un code", '<ol class="small" style="padding-left:4mm"><li>Ouvrez le téléphone (haut de la croix directionnelle).</li><li>Maintenez <b>L1 + R1</b> (PS5) ou <b>LB + RB</b> (Xbox).</li><li>Entrez la séquence sur la croix directionnelle.</li></ol>', "OBS", s(70,68), "#b072ff", "🎮")}
{card("Conditions et conséquences", '<ul class="small"><li>Les codes se débloquent <b>après le générique de fin</b> de l\'histoire.</li><li>Ils <b>désactivent les trophées et les succès</b>.</li><li>Vous ne pouvez plus <b>sauvegarder</b> jusqu\'au redémarrage du jeu.</li></ul>', "OBS", s(70), "#e5243b", "⚠️")}
</div>
<div class="card accent" style="--acc:#ffd23f;text-align:center">
<div class="ctitle"><h4>💵 Argent : + 250 000 $</h4>{badge("OBS")}</div>
<div style="font-family:Inter Display;font-weight:900;font-size:20pt;letter-spacing:.12em;color:#ffd23f;margin:1.4mm 0">{arrows}</div>
<div class="small">Disponible après l'histoire principale · Source : {s(68)}</div></div>
<div class="card" style="border-style:dashed"><div class="ctitle"><h4>Les autres codes</h4>{badge("NC")}</div>
<p class="small">Les sources annoncent de 17 à 61 codes, et certaines séquences (parachute, pas de dégâts de chute…) diffèrent d'un site à l'autre. Nous ne publions que les codes recoupés. Les autres seront ajoutés après vérification. <b>Aucun numéro de téléphone de triche</b> n'est connu à ce jour {s(69)}.</p></div>
{tip("Gardez une <b>sauvegarde propre</b> avant d'utiliser un code, puisqu'on ne peut plus sauvegarder ensuite et que les trophées sont désactivés.", "Prudence", "warn", "💾")}'''
    book.add(7, body)


# ---------------------------------------------------------------------------
# PARTIE 8 — COLLECTIBLES
# ---------------------------------------------------------------------------
COLL = [
    ("Cartes à collectionner", "🃏", "480 cartes en 18 séries", "15 séries", "Trophée « Don't Touch My Deck » à 3 séries", "OBS", (34, 36)),
    ("Scans WAiNK (monuments, curiosités, sculptures)", "📷", "89 à 112 lieux selon les sources", "100 scans", "Scannez avec l'application WAiNK", "OBS", (27, 36)),
    ("Cocaine Flamingos", "🦩", "125", "100", "—", "OBS", (30, 36)),
    ("Découvertes sous-marines", "🤿", "33 (7 séries d'épaves)", "33", "Après la mission « Island Dreams » ; lien avec Kenton", "OBS", (27, 35)),
    ("Spots de méditation", "🧘", "18", "15", "—", "OBS", (35, 36)),
    ("Paniers de basket", "🏀", "100", "90", "—", "OBS", (30,)),
    ("Animaux étudiés", "🐾", "255 entrées", "100", "Jumelles ou lunette ; la chasse n'est pas requise", "OBS", (27,)),
    ("Véhicules scannés", "🚗", "277 modèles de base", "200", "Avec WAiNK", "OBS", (27,)),
    ("Lectures (magazines, livres, BD)", "📚", "27, plus 7 échanges de livres", "?", "—", "NC", (36,)),
    ("Styles (tatouages de magazine, montres de luxe)", "⌚", "79", "?", "—", "NC", (36,)),
    ("Sauts / cascades", "🛹", "130 à 397 selon les sources", "?", "Chiffres contradictoires", "NC", (33, 36)),
]


def part8(book):
    opener(book, 8, "Collectibles", "Toutes les catégories d'objets à collectionner documentées depuis la sortie, avec leur total, le seuil requis pour le 100 % et les récompenses connues.",
           "sea", ["Tableau des catégories", "Fiches par catégorie", "Où chercher en priorité"], "p8")

    a = book.anchor("p8-tab", "Tableau des collectibles", 2)
    rows = "".join(f'<tr><td><span class="emoji">{e}</span> <b>{book.ix(n, "Collectible")}</b></td><td>{t}</td><td style="color:#38b6ff;font-weight:800">{r}</td><td>{badge(st)}</td></tr>'
                   for n, e, t, r, _, st, _ in COLL)
    body = f'''{a}<h2 class="title"><small style="color:#38b6ff">INVENTAIRE</small>Collectibles</h2>
<p class="small">Rockstar <b>n'a pas publié</b> de liste officielle ni de total de collectibles. Les chiffres ci-dessous viennent des guides publiés depuis la sortie et peuvent encore bouger {s(36,35)}.</p>
<table class="t" style="--acc:#38b6ff"><tr><th>Catégorie</th><th>Total</th><th>Pour 100 %</th><th>Statut</th></tr>{rows}</table>
{tip("Le menu <b>Progression / Statistiques</b> du jeu reste la référence : il affiche votre avancement réel dans chaque catégorie {s}.".replace("{s}", s(33)), "La référence", "gold", "📊")}'''
    book.add(8, body)

    a = book.anchor("p8-fiches", "Fiches collectibles", 2)
    cards = "".join(card(n, kv([("Total", t), ("Requis 100 %", r), ("Notes", note)]), st, s(*sr), "#38b6ff", e)
                    for n, e, t, r, note, st, sr in COLL[:8])
    body = f'''{a}<h2 class="title"><small style="color:#38b6ff">DÉTAIL</small>Fiches collectibles</h2>
<div class="grid2">{cards}</div>'''
    book.add(8, body)

    a = book.anchor("p8-prio", "Où chercher en priorité", 2)
    body = f'''{a}<h2 class="title"><small style="color:#38b6ff">MÉTHODE</small>Collecter efficacement</h2>
<div class="mapbox" style="margin:0 auto 2mm;width:62%">{leonida_map(markers=[("keys","🤿","#38b6ff"),("vice","📷","#38b6ff"),("grass","🦩","#38b6ff")])}</div>
<ol class="small" style="padding-left:4.5mm">
<li><b>Chapitre 1 (Keys)</b> : faites « Island Dreams » puis les plongées de Kenton. Les épaves comptent pour les découvertes sous-marines {s(35,40)}.</li>
<li><b>Partout</b> : gardez WAiNK à portée de main et scannez chaque monument et chaque nouveau modèle de voiture {s(27,87)}.</li>
<li><b>En exploration</b> : notez les spots de méditation et les paniers de basket. Il vous faut 15 spots sur 18 et 90 paniers sur 100 {s(30,35)}.</li>
<li><b>Les cartes</b> : visez 3 séries tôt pour le trophée, puis 15 séries pour le 100 % {s(34)}.</li>
</ol>
<p class="tiny muted">Les emplacements pièce par pièce (480 cartes, 125 flamants…) ne figurent pas dans cette version : les listes publiées ne sont pas encore stabilisées et nous refusons de publier des positions non vérifiées. Ils seront intégrés par régions dans les mises à jour. En attendant, les cartes interactives citées font le relais {s(54,89)}.</p>'''
    book.add(8, body)
