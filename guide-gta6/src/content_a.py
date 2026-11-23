# -*- coding: utf-8 -*-
"""Couverture, pages d'introduction, Partie 1 et Partie 2."""

from lib import (badge, tip, card, kv, scene, leonida_map, yt, REGIONS, PART_COLORS, E)
from sources import s


def opener(book, part, title, subtitle, kind, items, aid):
    col = PART_COLORS[part]
    a = book.anchor(aid, f"Partie {part} — {title}", 1)
    li = "".join(f"<li>{i}</li>" for i in items)
    body = (f'{a}<div class="ill" style="height:72mm;margin:-1mm -8mm 0;border:none;border-radius:0">{scene(kind, 420, 220)}</div>'
            f'<div class="opener" style="margin-top:4mm;display:flex;gap:4mm;align-items:flex-end">'
            f'<div class="numbig" style="color:{col}">{part:02d}</div>'
            f'<div><div style="font-size:7pt;letter-spacing:.2em;font-weight:800;color:{col}">PARTIE {part}</div>'
            f'<h1 style="font-size:{28 if max(len(w) for w in title.split()) > 9 else 40}pt">{title}</h1></div></div>'
            f'<p class="lead" style="margin-top:3mm">{subtitle}</p>'
            f'<div class="card" style="margin-top:2mm"><h4 style="color:{col}">Dans cette partie</h4><ul class="small">{li}</ul></div>')
    book.add(part, body)


# ---------------------------------------------------------------------------
def cover(book):
    body = (f'<div style="position:absolute;inset:0">{scene("cover", 560, 794, label="")}</div>'
            '<div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(10,5,15,.15) 0%, rgba(10,5,15,.0) 40%, rgba(10,5,15,.85) 78%, #0b0a10 100%)"></div>'
            '<div style="position:absolute;top:12mm;left:10mm;right:10mm;display:flex;justify-content:space-between;font-size:6.5pt;letter-spacing:.18em;font-weight:800">'
            '<span>GUIDE NON OFFICIEL</span><span style="color:#ffd23f">ÉDITION PREMIUM · FR</span></div>'
            '<div style="position:absolute;left:10mm;right:10mm;bottom:22mm">'
            '<div style="font-family:Inter Display;font-weight:900;font-size:14pt;letter-spacing:.32em;color:#ffb36b">LE GUIDE ULTIME</div>'
            '<div style="font-family:Inter Display;font-weight:900;font-size:66pt;line-height:.82;letter-spacing:-.03em;'
            'background:linear-gradient(90deg,#ff3d6e,#ff7a1a 55%,#ffd23f);-webkit-background-clip:text;color:transparent">GTA&nbsp;VI</div>'
            '<div style="font-family:Inter Display;font-weight:800;font-size:13pt;margin-top:2mm">Leonida &amp; Vice City de A à Z</div>'
            '<div style="margin-top:3mm;font-size:7.6pt;color:#e4dbe8;max-width:110mm">Carte des régions, véhicules rares, faune, missions, '
            'Easter Eggs, astuces, collectibles et checklist 100 % interactive. Chaque information est sourcée et porte un statut de fiabilité.</div>'
            '<div style="margin-top:4mm;display:flex;gap:2mm;flex-wrap:wrap">'
            '<span class="badge b-conf">✔ Confirmé</span><span class="badge b-obs">◉ Observé</span><span class="badge b-nc">? Non confirmé</span></div>'
            '<div style="margin-top:5mm;font-size:6pt;color:#9a93a6">Version 1.0 · mise à jour du 23 novembre 2026 · '
            'Guide indépendant, non édité, non approuvé et non affilié à Rockstar Games ou Take-Two Interactive.</div></div>')
    book.add(0, body, raw=True)


def disclaimer(book):
    a = book.anchor("avert", "Avertissement, méthode et statuts", 2)
    body = f'''{a}<h2 class="title"><small style="color:#ff7a1a">À LIRE AVANT DE COMMENCER</small>Méthode &amp; fiabilité</h2>
<p class="lead">Ce guide a une règle : <b>ne rien inventer</b>. Chaque information porte l'un des trois statuts ci-dessous. Les rumeurs sont regroupées dans des encadrés séparés.</p>
<div class="card accent" style="--acc:#1f9d55">{badge("CONF")} <b>&nbsp;Confirmé</b> : annoncé officiellement par Rockstar Games ou Take-Two (site officiel, bandes-annonces, communiqués), ou montré dans les vidéos officielles.</div>
<div class="card accent" style="--acc:#ff9f1a">{badge("OBS")} <b>&nbsp;Observé</b> : découverte faite en jeu après la sortie et documentée par la presse spécialisée ou par des guides communautaires, mais dont certains détails restent à confirmer (emplacement exact, compteur, conditions).</div>
<div class="card accent" style="--acc:#8d8698">{badge("NC")} <b>&nbsp;Non confirmé</b> : rumeur, théorie, information signalée par une seule source ou contredite par d'autres. Ne vous y fiez pas sans vérification.</div>
<h3 style="color:#ff7a1a">Comment ce guide a été réalisé</h3>
<ul class="small">
<li><b>Période de recherche :</b> du 19 au 23 novembre 2026, soit les quatre premiers jours après la sortie (19/11/2026).</li>
<li><b>Méthode :</b> les informations ont été croisées entre les communications officielles, la presse spécialisée et les guides communautaires publiés depuis la sortie. Toutes les sources sont numérotées <a href="#sources" style="color:#ffb36b">en fin de guide</a>, avec leur lien et une date de vérification.</li>
<li><b>Limite importante :</b> l'auteur n'a <b>pas</b> vérifié ces informations lui-même en jeu au moment de la rédaction. Les compteurs (collectibles, véhicules, missions) viennent de guides publiés après la sortie et <b>varient selon les sources</b>. Quand c'est le cas, nous indiquons l'écart.</li>
<li><b>Illustrations :</b> toutes les illustrations, tous les pictogrammes et toutes les cartes sont des <b>créations originales</b>. Il n'y a aucune capture d'écran du jeu. Les cartes sont des <b>schémas de repérage non à l'échelle</b>. Pour un positionnement au mètre près, utilisez la carte du jeu et les cartes interactives citées.</li>
<li><b>Exhaustivité :</b> ce guide <b>n'est pas encore exhaustif</b>. Le jeu vient de sortir et la communauté continue de faire des découvertes. Les rubriques incomplètes sont signalées et seront complétées dans les mises à jour (voir « Dernières découvertes »).</li>
</ul>
{tip("Les mentions <b>⚠ Spoilers</b> signalent les pages qui révèlent des éléments de l'histoire (titres de chapitres et de missions, événements). Vous pouvez les sauter sans perdre d'information pratique.", "Spoilers", "warn", "⚠️")}
<p class="tiny muted">Grand Theft Auto, GTA, Rockstar Games et les noms associés sont des marques de leurs propriétaires respectifs. Ce guide est une œuvre indépendante d'information et de critique.</p>'''
    book.add(0, body)


def how_to(book):
    a = book.anchor("mode", "Mode d'emploi du guide", 2)
    leg_map = leonida_map(markers=[("vice", "1"), ("grass", "2", "#18d4c4")], title=False)
    body = f'''{a}<h2 class="title"><small style="color:#18d4c4">NAVIGATION</small>Mode d'emploi</h2>
<div class="grid2">
<div>
<h3>Naviguer</h3>
<ul class="small">
<li>Le <b>sommaire</b> et tous les renvois sont <b>cliquables</b>.</li>
<li>En haut de chaque page : <b>☰ Sommaire</b>, <b>◎ Carte</b>, <b>☑ 100 %</b> et <b>A–Z</b> (index) pour vous déplacer en un geste.</li>
<li>Les signets du PDF (panneau latéral de votre lecteur) donnent accès à chaque partie.</li>
<li>Les numéros entre crochets, par exemple <a href="#src-1" style="color:#ffb36b">[1]</a>, renvoient vers la source correspondante.</li>
<li><span class="vlink">▶ Recherche vidéo</span> ouvre une recherche YouTube ciblée pour voir le secret en vidéo.</li>
</ul>
<h3>Cocher sa progression</h3>
<p class="small">Les cases <span class="cb" style="display:inline-block;vertical-align:middle"></span> de la Partie 9 se cochent dans Adobe Acrobat Reader (ordinateur, iOS, Android), dans Chrome, Edge ou Firefox, et dans Aperçu sur Mac. Pensez à <b>enregistrer</b> le PDF après avoir coché. Certains lecteurs simplifiés n'enregistrent pas les cases : dans ce cas, utilisez Acrobat Reader.</p>
</div>
<div>
<h3>Lire les cartes</h3>
<div class="mapbox">{leg_map}</div>
<p class="tiny muted" style="margin-top:1mm">Les épingles numérotées indiquent la <b>région</b> où se trouve un élément. Le repère précis (rue, bâtiment, heure) figure dans la fiche correspondante.</p>
</div></div>
{tip("Sur smartphone, tenez l'appareil à la verticale : chaque page fait le format A5 et se lit sans zoom. Sur tablette, utilisez l'affichage « page unique ».", "Lecture mobile", "", "📱")}'''
    book.add(0, body)


# ---------------------------------------------------------------------------
# PARTIE 1
# ---------------------------------------------------------------------------
def part1(book):
    opener(book, 1, "Bien démarrer", "Tout ce qu'il faut savoir avant et pendant vos premières heures à Leonida : le jeu, ses héros, son monde, ses systèmes et les erreurs à éviter.",
           "vice", ["Présentation du jeu et des éditions", "Personnages principaux et secondaires", "Le monde ouvert de Leonida",
                    "Système de recherche policière (Heat)", "Statistiques et progression", "Téléphone et applications",
                    "Argent : les trois poches", "Premières heures et erreurs de débutant"], "p1")

    # Présentation
    a = book.anchor("p1-pres", "Présentation du jeu", 2)
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">FICHE D'IDENTITÉ</small>Grand Theft Auto VI</h2>
<div class="ill" style="height:30mm;margin-bottom:2mm">{scene("vice", 420, 110)}</div>
<table class="t" style="--acc:#ff3d6e">
<tr><th>Élément</th><th>Information</th><th>Statut</th></tr>
<tr><td>Éditeur / studio</td><td>Rockstar Games (groupe Take-Two Interactive)</td><td>{badge("CONF")}</td></tr>
<tr><td>Sortie</td><td><b>Jeudi 19 novembre 2026</b>, déploiement à minuit heure locale selon les pays {s(3,4)}</td><td>{badge("CONF")}</td></tr>
<tr><td>Plateformes</td><td>PlayStation 5, Xbox Series X|S. <b>Aucune version PC annoncée</b> à la sortie {s(3,4)}</td><td>{badge("CONF")}</td></tr>
<tr><td>Report</td><td>Initialement prévu le 26 mai 2026, repoussé en novembre 2025 au 19/11/2026 {s(4)}</td><td>{badge("CONF")}</td></tr>
<tr><td>Prix (États-Unis)</td><td>Standard 79,99 $ · Ultimate 99,99 $ {s(6,7)}</td><td>{badge("CONF")}</td></tr>
<tr><td>Version physique</td><td>Contient un code de téléchargement plutôt qu'un disque complet {s(98,99)}</td><td>{badge("OBS")}</td></tr>
<tr><td>Cadre</td><td>L'État fictif de <b>Leonida</b>, avec sa métropole <b>Vice City</b> {s(1,2)}</td><td>{badge("CONF")}</td></tr>
<tr><td>Lancement</td><td>Environ <b>3,79 milliards $</b> de ventes au détail estimées en 24 h, selon Take-Two (rapporté par la presse) {s(5)}</td><td>{badge("CONF")}</td></tr>
<tr><td>Durée de l'histoire</td><td>Un prologue et 5 chapitres, environ 90 missions principales selon les tests {s(10,42)}</td><td>{badge("OBS")}</td></tr>
<tr><td>Taille de la carte</td><td>Pas de chiffre officiel. Les estimations tournent autour de 2 fois la carte de GTA V {s(9,13,14)}</td><td>{badge("NC")}</td></tr>
</table>
<h3>Standard ou Ultimate ?</h3>
<p class="small">Les deux éditions incluent le bonus de précommande <b>Vintage Vice City Pack</b>. Selon les guides, l'Ultimate ajoute des véhicules et des variantes d'armes exclusifs, des packs cosmétiques, un garage dédié (le <b>Paradise Garage</b>) et une mission secondaire {s(98,99,71)} {badge("OBS")}. Le contenu exact peut varier selon la plateforme et la boutique. Fiez-vous à la fiche de votre boutique.</p>'''
    book.add(1, body)

    # Personnages
    a = book.anchor("p1-perso", "Personnages principaux", 2)
    def perso(name, role, desc, st, src, col, init):
        book.ix(name, "Personnage")
        return (f'<div class="card accent" style="--acc:{col};display:flex;gap:2.6mm">'
                f'<div style="flex:0 0 13mm;height:13mm;border-radius:50%;background:linear-gradient(135deg,{col},#2a0f2f);display:flex;align-items:center;justify-content:center;'
                f'font-family:Inter Display;font-weight:900;font-size:13pt">{init}</div>'
                f'<div style="flex:1"><div class="ctitle"><h4>{name}</h4>{badge(st)}</div>'
                f'<div class="small" style="color:{col};font-weight:700;margin-bottom:.5mm">{role}</div>'
                f'<div class="small">{desc}</div><div class="src">Sources : {src}</div></div></div>')
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">LE DUO</small>Jason &amp; Lucia</h2>
<p class="small">GTA VI est le premier épisode de la série principale avec un <b>duo de héros jouables</b>. Rockstar présente l'histoire comme celle d'un couple qui se retrouve « au milieu d'une conspiration criminelle qui s'étend à tout l'État de Leonida » {s(1,2)}.</p>
{perso("Lucia Caminos", "Protagoniste jouable", "La deuxième bande-annonce la montre à sa sortie de prison, puis reprenant le crime aux côtés de Jason. C'est la première héroïne principale de la série moderne.", "CONF", s(1,2), "#ff3d6e", "LC")}
{perso("Jason Duval", "Protagoniste jouable", "Il cherche une « vie facile » et travaille pour des trafiquants locaux dans les Keys. Sa vie bascule quand il retrouve Lucia.", "CONF", s(1,2), "#ff7a1a", "JD")}
{tip("Les missions peuvent se jouer avec un seul des deux héros ou avec les deux ensemble. Chacun a ses propres statistiques à faire progresser (voir « Statistiques »).", "Duo jouable", "", "🎭")}
<p class="tiny muted">Sources : {s(12,20)}</p>'''
    book.add(1, body)

    a = book.anchor("p1-perso2", "Personnages secondaires", 2)
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">LE CASTING OFFICIEL</small>Seconds rôles</h2>
<div class="grid2">
{card(book.ix("Cal Hampton","Personnage"), '<p class="small">Ami de Jason et adepte des théories du complot. Il adore espionner les communications de la police. C\'est l\'un des associés de Brian Heder.</p>', "CONF", s(1,94,95), "#18d4c4", "🛰️")}
{card(book.ix("Boobie Ike","Personnage"), '<p class="small">Ancien « hustler » devenu figure de l\'immobilier et des affaires à Vice City. Il possède le club <b>Jack of Hearts</b>.</p>', "CONF", s(1,96), "#ffd23f", "🃏")}
{card(book.ix("Dre'Quan Priest","Personnage"), '<p class="small">Associé de Boobie Ike. Il s\'occupe de musique et voit dans le duo Real Dimez sa chance avec le label <b>Only Raw Records</b>.</p>', "CONF", s(1,96), "#b072ff", "🎤")}
{card(book.ix("Real Dimez","Personnage"), '<p class="small">Duo de rappeuses (<b>Bae-Luxe</b> et <b>Roxy</b>), connu pour ses morceaux provocants et sa présence omniprésente sur les réseaux sociaux.</p>', "CONF", s(1,94), "#ff3d8b", "💎")}
{card(book.ix("Brian Heder","Personnage"), '<p class="small">Propriétaire et trafiquant de drogue de longue date, lié à Jason et à Cal.</p>', "CONF", s(1,94), "#7bd651", "🚤")}
{card(book.ix("Raul Bautista","Personnage"), '<p class="small">Braqueur expérimenté, présenté sur le site officiel. Nous n\'avons pas trouvé d\'autres détails vérifiables.</p>', "CONF", s(1,95), "#e5243b", "🏦")}
</div>
<h3>Contacts de quêtes repérés après la sortie</h3>
<p class="small">Les guides publiés depuis la sortie citent ces donneurs de missions secondaires. Ils sont détaillés dans la <a href="#p5-sf" style="color:#ffb36b">Partie 5</a> {badge("OBS")} :
<span class="pill">{book.ix("Moses","Personnage")} (receleur de voitures)</span><span class="pill">{book.ix("Yasmani","Personnage")} (braquages)</span><span class="pill">{book.ix("Shirley","Personnage")} (rhum, scooters)</span>
<span class="pill">{book.ix("Kirk","Personnage")} (Skunk Ape)</span><span class="pill">{book.ix("Kenton","Personnage")} (épaves)</span><span class="pill">{book.ix("Kyle","Personnage")} (épandage agricole)</span>
<span class="pill">{book.ix("Bret Vogel","Personnage")} (chasse)</span><span class="pill">{book.ix("Billy","Personnage")} (Thrillbilly Mud Club)</span><span class="pill">{book.ix("Yago","Personnage")} (courses de rue)</span>
<span class="pill">{book.ix("Pilot Pete","Personnage")} (livraisons aériennes)</span><span class="pill">{book.ix("Donnie","Personnage")} (receleur, chapitre 1)</span></p>
<p class="src">Sources : {s(40,41,42,38)}</p>'''
    book.add(1, body)

    # Monde ouvert
    a = book.anchor("p1-monde", "Le monde ouvert de Leonida", 2)
    rows = "".join(f'<tr><td><b style="color:{r["c"]}">{E(r["name"])}</b></td><td>{d}</td></tr>' for r, d in (
        (REGIONS["vice"], "Métropole néon : plages, vie nocturne, gratte-ciel, port de croisière."),
        (REGIONS["keys"], "Chapelet d'îles au sud. C'est là que se déroule le chapitre 1."),
        (REGIONS["grass"], "Marais et prairies inondées, territoire des alligators."),
        (REGIONS["port"], "Ville côtière du golfe, un peu oubliée, avec son circuit automobile."),
        (REGIONS["ambrosia"], "Arrière-pays agricole et industriel, autour d'une raffinerie de sucre."),
        (REGIONS["kalaga"], "Parc national sauvage : forêts, lacs, chasse et pêche."),
    ))
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">LE TERRAIN DE JEU</small>L'État de Leonida</h2>
<div class="grid2">
<div class="mapbox">{leonida_map()}</div>
<div><p class="small">Leonida est un État fictif inspiré de la Floride. Rockstar y a officiellement nommé <b>six régions</b> {s(1,2,89)} {badge("CONF")}.</p>
<table class="t" style="--acc:#ff3d6e;font-size:6.8pt"><tr><th>Région</th><th>En bref</th></tr>{rows}</table></div></div>
<h3>Ce qu'il faut savoir</h3>
<ul class="small">
<li>Le jeu introduit des <b>comtés</b> nommés : Vice-Dale, Mariana, Leonard, Kelly… Les guides s'en servent pour situer les lieux, mais leurs limites exactes ne sont pas officiellement documentées {s(89,50)} {badge("OBS")}.</li>
<li>L'histoire vous fait voyager : les Keys (chapitre 1), puis Port Gellhorn (chapitre 2), puis Vice City (chapitres 3 à 5) {s(45,46,47)} {badge("OBS")}.</li>
<li>Selon les guides, une partie du contenu secondaire est <b>liée à un chapitre</b> et peut devenir indisponible ensuite. Repérez les mentions « limité dans le temps » dans la Partie 5.</li>
</ul>'''
    book.add(1, body)

    # Heat
    a = book.anchor("p1-heat", "Police : le système Heat", 2)
    stars = "".join('<span style="font-size:14pt;color:#ffd23f">★</span>' for _ in range(6))
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">MÉCANIQUE CLÉ</small>Police &amp; « Heat »</h2>
<div class="card" style="text-align:center">{stars}<div class="small muted">Six niveaux de recherche selon les présentations du jeu {s(15)} {badge("OBS")}</div></div>
<p class="small">GTA VI sépare deux notions : les <b>étoiles</b> indiquent l'intensité de la réponse policière, et le <b>Heat</b> indique ce que la police sait de vous : votre tenue, votre apparence, votre véhicule de fuite {s(15,16,18)} {badge("OBS")}.</p>
<div class="grid2">
{card("Couleur des étoiles", '<ul class="small"><li><b>Blanches cerclées de noir</b> : la police enquête mais ne sait pas encore que c\'est vous.</li><li><b>Rouges</b> : vous avez semé la police, mais elle reprend la poursuite si elle vous identifie.</li></ul>', "OBS", s(16), "#ffd23f")}
{card("Icônes de Heat", '<p class="small">Des icônes sous les étoiles indiquent ce qui vous trahit (vêtements, véhicule…). Plus vous en supprimez, plus il est facile de quitter la zone.</p>', "OBS", s(17,18), "#ff3d6e")}
</div>
<h3>Semer la police : la méthode</h3>
<ol class="small" style="padding-left:4.5mm">
<li><b>Coupez la ligne de vue</b> : ruelles, parkings, tunnels. Les zones couvertes sont efficaces contre les hélicoptères {s(19)}.</li>
<li><b>Changez de véhicule</b> : votre voiture recherchée vous signale. Prenez-en une garée, ou un bateau {s(19)}.</li>
<li><b>Changez de tenue</b> pour faire disparaître l'icône « vêtements » {s(19,17)}.</li>
<li><b>Sortez de la zone de recherche</b> affichée sur la carte {s(15,19)}.</li>
<li><b>Ne tirez pas</b> : les coups de feu gardent la police sur vous {s(19)}.</li>
</ol>
{tip("Le Heat peut <b>rester attaché à une zone</b> même après la disparition des étoiles {s} : évitez d'y retourner tout de suite avec la même voiture ou la même tenue.".replace("{s}", s(16)), "À savoir", "warn", "🚨")}
<p class="tiny muted">Désaccords entre sources : la taille de la zone à 6 étoiles (régionale ou toute la carte) et l'effacement immédiat du niveau quand on coupe la ligne de vue ne sont pas tranchés {badge("NC")}. Aucun système de pot-de-vin n'est confirmé {s(19)}.</p>'''
    book.add(1, body)

    # Stats + téléphone
    a = book.anchor("p1-stats", "Statistiques et progression", 2)
    def bar(label, col, w):
        return (f'<div style="margin:1mm 0"><div class="small" style="display:flex;justify-content:space-between"><b>{label}</b></div>'
                f'<div style="height:2.4mm;border-radius:2mm;background:rgba(255,255,255,.08)"><div style="height:100%;width:{w}%;border-radius:2mm;background:{col}"></div></div></div>')
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">PROGRESSION</small>Statistiques</h2>
<div class="grid2"><div>
<p class="small">Jason et Lucia ont les <b>trois mêmes statistiques</b>, et chacun les fait progresser <b>séparément</b> {s(20,21)} {badge("OBS")}. Elles sont visibles dans le menu du personnage.</p>
{bar("❤ Santé (Health)", "#e5243b", 70)}{bar("⚡ Endurance (Stamina)", "#ffd23f", 55)}{bar("◎ Concentration (Focus)", "#18d4c4", 40)}
<p class="tiny muted">Jauges illustratives. Un guide parle plutôt de « Strength / Cardio / Focus » : l'intitulé exact peut dépendre de la langue du jeu {s(20)}.</p>
</div><div>
{card("Focus : le ralenti", '<p class="small">La jauge de Focus permet de <b>ralentir le temps</b> en combat. Selon les guides, elle met aussi en évidence les menaces, les objets de valeur et les poissons quand vous pêchez.</p>', "OBS", s(20,65), "#18d4c4")}
</div></div>
<h3>Comment s'entraîner</h3>
<ul class="small">
<li><b>Dès le début :</b> il y a des haltères sur la terrasse de la maison de Jason {s(20)} {badge("OBS")}.</li>
<li><b>Ensuite :</b> abonnement en salle de sport (le jeu en propose officiellement) {s(20,93)}.</li>
<li><b>Au quotidien :</b> courir, faire du vélo et nager font progresser l'endurance {s(20,21)}.</li>
</ul>
{tip("Entraînez <b>les deux héros</b> : comme les statistiques sont séparées, un Jason entraîné ne rend pas Lucia plus résistante.", "Conseil", "", "🏋️")}
<p class="tiny muted">Aucune statistique de « conduite » ou de « tir » n'apparaît dans les guides publiés après la sortie. Les listes qui en mentionnent datent d'avant la sortie {badge("NC")}.</p>'''
    book.add(1, body)

    a = book.anchor("p1-tel", "Téléphone et applications", 2)
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">VOTRE MEILLEUR OUTIL</small>Le téléphone</h2>
<div class="grid2">
{card(book.ix("WAiNK","Application"), '<p class="small">Scanner : visez une voiture (touche haut de la croix directionnelle) pour connaître ses <b>serrures</b>, son <b>alarme</b>, son <b>traceur</b> et sa <b>valeur</b>. Il sert aussi à scanner les monuments et les œuvres comptés pour le 100 %.</p>', "OBS", s(87,88), "#ff7a1a", "📷")}
{card(book.ix("BuckMe","Application"), '<p class="small">Application bancaire, débloquée par la mission du chapitre 1 « Buck Me ». L\'argent déposé est <b>protégé en cas de mort</b>, contrairement à l\'argent liquide.</p>', "OBS", s(87,25), "#7bd651", "🏦")}
{card(book.ix("Snapmatic","Application"), '<p class="small">Fil social et photo du jeu, l\'équivalent d\'Instagram, cité par plusieurs guides.</p>', "OBS", s(87,88), "#ff3d8b", "🤳")}
{card("Vice City Real Estate", '<p class="small">Application immobilière pour acheter les garages (voir <a href="#p3-garages" style="color:#ffb36b">Partie 3</a>).</p>', "OBS", s(71,73), "#38b6ff", "🏠")}
</div>
<div class="card" style="--acc:#8d8698"><div class="ctitle"><h4>Non confirmé</h4>{badge("NC")}</div>
<p class="small">LifeInvader et Bleeter, les réseaux des anciens GTA, n'apparaissent pas dans les listes d'applications confirmées. Le nombre total d'applications varie de 7 à 14 selon les sources {s(87,88)}.</p></div>
<h3>Radio : les stations</h3>
<p class="small">Selon les crédits relevés par la presse, il y a <b>21 stations musicales et 2 stations de débat</b> (The Wipe, WKTT) {s(85,86)} {badge("OBS")}. Parmi elles :
<span class="pill">Vice City FM</span><span class="pill">Flash FM</span><span class="pill">V-Rock</span><span class="pill">Emotion 98.3</span><span class="pill">Radio La Ola</span><span class="pill">Cocoteo FM</span><span class="pill">Back Country Radio</span><span class="pill">Gloriana Blues</span><span class="pill">Leonida Jazz Radio</span><span class="pill">Dirty South Classics</span><span class="pill">Vice City Rap Radio</span><span class="pill">Worldwide FM</span><span class="pill">AfroBank FM</span><span class="pill">Honey FM</span><span class="pill">Kaleidoscope FM</span><span class="pill">Stockyard FM</span><span class="pill">Symphony FM</span><span class="pill">The Chamber 106.6</span><span class="pill">Radio On-U</span><span class="pill">CircoLoco Records Radio</span></p>
<p class="small">La station <b>The Vault Radio</b> (house, électro) serait à débloquer {s(86)} {badge("NC")}.</p>'''
    book.add(1, body)

    # Argent
    a = book.anchor("p1-argent", "Le système d'argent", 2)
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">ÉCONOMIE</small>Argent : protégez vos gains</h2>
<div class="grid3">
{card("Liquide (Pocket Cash)", '<p class="small">L\'argent que vous avez sur vous. Vous le <b>perdez</b> si vous mourez ou si vous êtes arrêté.</p>', "OBS", s(23,25), "#e5243b", "💵")}
{card("Compte BuckMe", '<p class="small">L\'argent en banque, à l\'abri en cas de mort. Un guide indique que les dépôts ne se feraient qu\'aux distributeurs.</p>', "OBS", s(87,25), "#7bd651", "🏦")}
{card("Family Savings", '<p class="small">L\'épargne commune du duo. Selon un guide, c\'est la seule réserve conservée à la fin du chapitre 1.</p>', "NC", s(25), "#ffd23f", "🐷")}
</div>
{tip("Plusieurs guides conseillent de <b>ne pas trop accumuler d'argent au chapitre 1</b>. Un guide affirme même que l'argent liquide et le solde BuckMe sont remis à zéro à la fin du chapitre {s}. Profitez de ce chapitre pour explorer et collectionner plutôt que pour accumuler.".replace("{s}", s(25,23)), "Erreur à éviter", "warn", "⛔")}
<h3>La progression de l'argent, chapitre par chapitre</h3>
<table class="t" style="--acc:#ff3d6e">
<tr><th>Chapitre</th><th>Méthode</th><th>Gains signalés</th><th>Statut</th></tr>
<tr><td>1 (Keys)</td><td>Petits braquages de magasins</td><td>500 à 3 000 $</td><td>{badge("OBS")}</td></tr>
<tr><td>1 (Keys)</td><td>Mission de rhum de {book.ix("Shirley","Personnage")} (pillage de contrebandiers)</td><td>≈ 2 600 $</td><td>{badge("NC")}</td></tr>
<tr><td>2 (Port Gellhorn)</td><td>Revente de voitures volées à <b>Moses</b> (voitures sans traceur)</td><td>Meilleure méthode au début selon les guides</td><td>{badge("OBS")}</td></tr>
<tr><td>3 (Vice City)</td><td>Receleurs (stupéfiants, bijoux, billets marqués)</td><td>Variable</td><td>{badge("OBS")}</td></tr>
<tr><td>3 (Vice City)</td><td>Livraisons de la « Wish List » de Randy</td><td>30 000 $ et plus chacune</td><td>{badge("NC")}</td></tr>
<tr><td>3</td><td>Braquages de bijouteries, de distributeurs et de prêteurs sur gages (Yasmani)</td><td>Bons gains</td><td>{badge("OBS")}</td></tr>
<tr><td>Fin du 4</td><td>Coffres-forts de banque, après « That's Where The Money Is… » (Yasmani)</td><td>Méthode la plus rentable</td><td>{badge("OBS")}</td></tr>
</table>
<p class="src">Sources : {s(22,23,24,26,38,39)}. Les montants horaires annoncés par certains sites (35 000 à 60 000 $/h) ne sont pas recoupés {badge("NC")}.</p>'''
    book.add(1, body)

    # Premières heures + erreurs
    a = book.anchor("p1-debut", "Premières heures et erreurs de débutant", 2)
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">CHECK-LIST DE DÉPART</small>Vos premières heures</h2>
<div class="ill" style="height:24mm;margin-bottom:2mm">{scene("keys", 420, 90)}</div>
<ol class="small" style="padding-left:4.5mm">
<li><b>Récupérez la canne à pêche</b> : elle est gratuite, sur le ponton derrière la maison de Jason à <b>Key Lento</b>, et figure aussi dans l'onglet Équipement de la roue d'armes {s(65,67)} {badge("OBS")}.</li>
<li><b>Utilisez les haltères</b> sur la terrasse de Jason pour commencer à gagner en santé et en endurance {s(20)}.</li>
<li><b>Débloquez BuckMe</b> (mission « Buck Me ») et déposez votre argent liquide dès que possible {s(87)}.</li>
<li><b>Scannez tout avec WAiNK</b> : les voitures (traceur, valeur) et les monuments, qui comptent pour le 100 % {s(87,27)}.</li>
<li><b>Notez les quêtes secondaires du chapitre 1</b> : Kirk, Shirley, Kenton et Cal. Selon les guides, certaines ne sont disponibles qu'à ce chapitre {s(40,35)}.</li>
<li><b>Après « Island Dreams »</b>, les découvertes sous-marines se débloquent {s(35)} {badge("OBS")}.</li>
</ol>
<h3 style="color:#e5243b">Les erreurs de débutant</h3>
<div class="grid2">
{card("Se promener avec beaucoup de liquide", '<p class="small">En cas de mort ou d\'arrestation, l\'argent liquide est perdu.</p>', "OBS", s(23,25), "#e5243b", "💸")}
{card("Garder une voiture « chaude »", '<p class="small">Le Heat retient votre véhicule. Changez de voiture après un délit.</p>', "OBS", s(16,19), "#e5243b", "🚗")}
{card("Vendre une voiture avec traceur", '<p class="small">Moses refuse les voitures équipées d\'un traceur. Vérifiez avec WAiNK avant de voler.</p>', "OBS", s(38,39), "#e5243b", "📡")}
{card("Oublier les quêtes limitées", '<p class="small">La chaîne de courses de Yago est signalée comme limitée dans le temps.</p>', "OBS", s(41), "#e5243b", "⏳")}
</div>
<p class="tiny muted">Ce guide ne publie que des conseils documentés. Cette liste sera enrichie dans les mises à jour.</p>'''
    book.add(1, body)


# ---------------------------------------------------------------------------
# PARTIE 2
# ---------------------------------------------------------------------------
REGION_PAGES = [
    ("vice", "Vice City", "vice", "#ff3d6e",
     "Métropole néon de Leonida : plages, Art déco, gratte-ciel, vie nocturne et port de croisière. C'est le décor principal des chapitres 3 à 5.",
     ["Côte sud-est de Leonida, comté de Vice-Dale selon les guides",
      "Quartiers cités : Downtown, Ocean Beach, Little Cuba, Crosstown, Bayside, Stockyard, Salton, Decor District"],
     "Accessible librement une fois l'histoire arrivée à Vice City. Ponts et autoroutes depuis le continent ; port et aéroport.",
     ["Ocean Beach et sa promenade néon", "Le club Jack of Hearts (Boobie Ike)", "Downtown : Sahara Arena, Vice City Arts Center, tour Megamundo, grande roue",
      "Aéroport international et port de croisière", "Easter Egg : l'appartement de Dexter (voir Partie 6)"],
     "CONF", [1, 2, 89, 91, 92]),
    ("keys", "Leonida Keys", "keys", "#38b6ff",
     "Chapelet d'îles reliées par des ponts au sud de l'État. Le chapitre 1, « Just Like Paradise », s'y déroule autour de la maison de Jason.",
     ["Sud de Leonida", "Repères cités : Key Lento (maison de Jason), Gambit Bay (pêche, Cool Dog)"],
     "Zone de départ de l'histoire.",
     ["Ponton de Key Lento : la canne à pêche gratuite", "Plongée, épaves et découvertes sous-marines (après « Island Dreams »)",
      "Quêtes de Shirley, Kenton et Cal", "Rencontre aléatoire : le chien en jet-ski"],
     "CONF", [1, 2, 45, 65]),
    ("grass", "Grassrivers", "grass", "#5f9e3a",
     "Immense zone de marais et de prairies inondées, inspirée des Everglades. C'est le royaume des alligators et des hydroglisseurs.",
     ["Centre-sud de Leonida", "Repères cités : Cottonmouth Lake, Gullet Marsh (comté de Mariana)"],
     "Par la route depuis les Keys ou Vice City, ou en hydroglisseur sur l'eau.",
     ["Alligators et faune des marais", "Spots de pêche (Candy Fish signalé)", "Easter Egg : le Skunk Ape (Bigfoot local)",
      "Rumeur : un crabe géant dans Gullet Marsh (non confirmé)"],
     "CONF", [1, 2, 50, 57]),
    ("port", "Port Gellhorn", "port", "#a05ac8",
     "Ville balnéaire un peu déclinante sur la côte du golfe. Le chapitre 2, « Paradise Lost », s'y déroule.",
     ["Côte ouest et nord-ouest (golfe)", "Repères cités : Gellhorn International Raceway, comté de Kelly à l'est"],
     "Débloquée par l'histoire au chapitre 2.",
     ["Moses, le receleur de voitures", "Gellhorn International Raceway (garage Qwick-Fix)", "Vide-grenier au sud de la ville : le chapeau d'Arthur Morgan",
      "Easter Egg : l'enlèvement par un OVNI sur les routes du comté de Kelly"],
     "CONF", [1, 2, 38, 53, 75]),
    ("ambrosia", "Ambrosia", "ambrosia", "#d98a1f",
     "Arrière-pays agricole et industriel de Leonida, dominé par une raffinerie de sucre et entouré de champs.",
     ["Intérieur des terres, au nord du centre"],
     "Par la route, en traversant l'arrière-pays.",
     ["Paysages ruraux et routes de campagne", "Missions agricoles (Kyle, épandage), signalées par les guides"],
     "CONF", [1, 2, 40]),
    ("kalaga", "Mount Kalaga National Park", "kalaga", "#3a9a7a",
     "Parc national sauvage : forêts, collines, lacs et rivières. C'est le terrain idéal pour la chasse, la pêche et les activités de plein air.",
     ["Nord de Leonida"],
     "Par la route du nord.",
     ["Cougars et cerfs (faune signalée)", "Chasse : quête de Bret Vogel", "Pêche en eau douce"],
     "CONF", [1, 2, 62]),
]


def part2(book):
    opener(book, 2, "Carte & lieux", "Les six régions officielles, les quartiers de Vice City, les lieux à ne pas manquer et les repères des découvertes.",
           "keys", ["Carte générale de Leonida", "Fiches des 6 régions", "Vice City : quartiers et lieux phares",
                    "Lieux incontournables", "Où trouver les secrets (vue d'ensemble)"], "p2")
    a = book.anchor("carte", "Carte générale de Leonida", 2)
    mk = [("vice", "1"), ("keys", "2"), ("grass", "3"), ("port", "4"), ("ambrosia", "5"), ("kalaga", "6")]
    body = f'''{a}<h2 class="title"><small style="color:#18d4c4">VUE D'ENSEMBLE</small>Carte de Leonida</h2>
<div class="mapbox" style="width:78%;margin:0 auto">{leonida_map(markers=mk)}</div>
<div class="grid3" style="margin-top:2mm">''' + "".join(
        f'<a href="#reg-{k}" class="card" style="padding:1.6mm 2mm"><b style="color:{REGIONS[k]["c"]}">{n}. {E(REGIONS[k]["name"])}</b><div class="tiny muted">Voir la fiche →</div></a>'
        for k, n in mk) + f'''</div>
<p class="tiny muted">Schéma de repérage original, non à l'échelle : seules les positions relatives des régions sont indiquées. Pour la précision au mètre, consultez la carte du jeu ou une carte interactive {s(89,54,74)}.</p>'''
    book.add(2, body)

    for key, name, sc, col, desc, reperes, acces, decouv, st, src in REGION_PAGES:
        book.ix(name, "Lieu")
        a = book.anchor(f"reg-{key}", name, 3)
        lis = "".join(f"<li>{d}</li>" for d in decouv)
        rep = "".join(f"<li>{r}</li>" for r in reperes)
        body = f'''{a}<h2 class="title"><small style="color:{col}">RÉGION OFFICIELLE</small>{name}</h2>
<div class="ill" style="height:38mm">{scene(sc, 420, 150)}</div>
<div class="grid2" style="margin-top:2mm;grid-template-columns:1.05fr .95fr">
<div><div class="ctitle" style="display:flex;justify-content:space-between"><h4 style="color:{col}">Présentation</h4>{badge(st)}</div>
<p class="small">{desc}</p>
<h4 style="color:{col}">Repères</h4><ul class="small">{rep}</ul>
<h4 style="color:{col}">Accès</h4><p class="small">{acces}</p></div>
<div class="mapbox">{leonida_map(highlight=[key], markers=[(key, "★", col)])}</div></div>
<div class="card accent" style="--acc:{col}"><h4>À découvrir</h4><ul class="small">{lis}</ul>
<div class="src">Sources : {s(*src)} · Les éléments de jeu détaillés sont {badge("OBS")} sauf mention contraire.</div></div>'''
        book.add(2, body)

    # Vice City lieux
    a = book.anchor("p2-vice", "Vice City : lieux phares", 2)
    places = [
        ("Ocean Beach", "La plage la plus touristique, avec sa promenade aux enseignes néon. Allez-y de jour pour la foule, de nuit pour les néons.", "OBS", s(91,92)),
        ("Downtown", "Le cœur des gratte-ciel : Sahara Arena, Vice City Arts Center, tour Megamundo, parc du front de mer et grande roue.", "OBS", s(91)),
        ("Jack of Hearts", "Club de strip-tease haut de gamme de Boobie Ike, un lieu central de l'histoire.", "CONF", s(1,91)),
        ("Aéroport international de Vice City", "Salon d'aviation privée, tarmac, hangars et avions.", "OBS", s(91)),
        ("VC Port", "Grand port d'escale des paquebots de croisière.", "OBS", s(91)),
        ("Stockyard", "Le quartier de la culture automobile et du Vice City plus populaire.", "OBS", s(91)),
        ("Tisha-Wocka", "Quartier connu pour son marché aux puces et ses contrefaçons.", "OBS", s(91)),
        ("Little Cuba", "Quartier de la communauté cubaine, célèbre pour ses boulangeries.", "OBS", s(89,91)),
        ("La Perle", "Quartier culturel haïtien de Vice City.", "OBS", s(91)),
    ]
    cards = "".join(card(book.ix(n, "Lieu"), f'<p class="small">{d}</p>', st, sr, "#ff3d6e", "📍") for n, d, st, sr in places)
    body = f'''{a}<h2 class="title"><small style="color:#ff3d6e">LA MÉTROPOLE</small>Vice City : lieux phares</h2>
<div class="grid2">{cards}</div>
<div class="card" style="--acc:#8d8698"><div class="ctitle"><h4>Retour des lieux de GTA Vice City (2002) ?</h4>{badge("NC")}</div>
<p class="small">Certains guides citent le retour de Vice Point, Washington Beach, Starfish Island et de l'Ocean View Hotel. Nous ne l'avons pas recoupé {s(91,92)}.</p></div>'''
    book.add(2, body)

    # Lieux incontournables + carte des découvertes
    a = book.anchor("p2-top", "Lieux incontournables et carte des découvertes", 2)
    mk2 = [("vice", "A", "#ff3d6e", (-14, -12)), ("vice", "B", "#ffd23f", (14, 22)), ("keys", "C", "#38b6ff", (-40, -2)),
           ("grass", "D", "#7bd651", (-12, -10)), ("port", "E", "#b072ff", (-14, 0)), ("port", "F", "#ffd23f", (40, 8)),
           ("kalaga", "G", "#3a9a7a", (0, 0))]
    legend = [("A", "Ocean Beach & Downtown (Vice City)", "#p2-vice"), ("B", "Appartement de Dexter (Easter Egg)", "#ee-dexter"),
              ("C", "Key Lento & Gambit Bay (pêche, Cool Dog)", "#ee-dog"), ("D", "Marais de Cottonmouth Lake (Skunk Ape)", "#ee-skunk"),
              ("E", "Port Gellhorn : vide-grenier et circuit", "#ee-hat"), ("F", "Comté de Kelly : OVNI (de nuit)", "#ee-ufo"),
              ("G", "Mount Kalaga : faune sauvage, chasse", "#p4-hab")]
    lg = "".join(f'<a href="{h}" style="display:flex;gap:1.6mm;padding:.6mm 0;border-bottom:.25mm dotted rgba(255,255,255,.15)"><b style="color:#ffd23f;width:4mm">{l}</b><span class="small">{t}</span></a>' for l, t, h in legend)
    body = f'''{a}<h2 class="title"><small style="color:#18d4c4">À VISITER ABSOLUMENT</small>Lieux &amp; découvertes</h2>
<div class="grid2" style="grid-template-columns:1.1fr .9fr"><div class="mapbox">{leonida_map(markers=mk2)}</div>
<div>{lg}<p class="tiny muted" style="margin-top:1.4mm">Épingles placées au niveau de la région. Le repère précis figure dans chaque fiche (lien cliquable).</p></div></div>
{tip("Pour un repérage exact, combinez ce guide avec la carte du jeu et les filtres « Easter Eggs » et « Garages » de la carte interactive de GTABase {s}.".replace("{s}", s(54,74)), "Carte interactive", "", "🗺️")}'''
    book.add(2, body)
