# -*- coding: utf-8 -*-
"""Parties 3 (véhicules), 4 (animaux), 5 (missions & activités)."""

from lib import badge, tip, card, kv, scene, leonida_map, vicon, yt, E
from sources import s
from content_a import opener


# ---------------------------------------------------------------------------
# PARTIE 3 — VÉHICULES
# ---------------------------------------------------------------------------
RARE = [
    ("Pegassi Infernus", "super", "Supersportive", "vice", "Niveau 7 du parking du <b>commissariat de Crosstown</b> (Vice City). Les guides indiquent NW 9th St ou NE 9th Street.",
     "Vol : il faut se faufiler entre les policiers.", "OBS", s(75, 77)),
    ("Pegassi Vitello", "super", "Supersportive", None, "Villa de <b>Flamingo Parkway</b>, à Waning Sands.", "Vol : passez par-dessus la clôture.", "OBS", s(75)),
    ("Bravado Gauntlet Hellfire", "muscle", "Muscle car", None, "Casse <b>M7</b> près de Galerina Street, à l'est du <b>Boone Speedway</b>.", "Vol.", "OBS", s(75)),
    ("Pegassi Tempesta", "super", "Supersportive", "vice", "Le long de <b>NE 3rd Street</b> (Vice City), pendant une scène de remorquage (la voiture est sur la dépanneuse).", "Récupérez-la sur la dépanneuse.", "OBS", s(75)),
    ("Ascot Paragon", "car", "Sport", None, "Devant le <b>Banana Hole Main Bar</b> sur Shore Drive. Aperçue en soirée.", "Vol. Apparition signalée le soir.", "OBS", s(77)),
    ("Pegassi Toros", "suv", "SUV de luxe", None, "Devant les <b>Pegassi Residences</b>, sur Bayside Drive (Tequesta). Aperçu en soirée.", "Vol. Apparition signalée le soir.", "OBS", s(77)),
    ("Annis Drifter Elegy", "car", "Sport (drift)", "port", "Dans l'atelier <b>Qwick-Fix</b> derrière la piste de dragster du <b>Gellhorn International Raceway</b> (Port Gellhorn).", "Vol. L'emplacement est approximatif selon la source.", "OBS", s(78)),
    ("Pegassi Charred Torus (dorée)", "super", "Supersportive", None, "Garage d'une propriété de <b>Casanova Island</b> (maison en bas au centre de l'île).", "Entrez dans le garage de la propriété.", "OBS", s(76)),
    ("Anarchist Dominator", "muscle", "Muscle car", None, "Toit du parking de <b>Dynamics Fitness</b>.", "Venez de jour.", "OBS", s(77)),
    ("Maibatsu '97 Penumbra FF", "car", "Sport (classique)", None, "Garage d'une maison sur <b>Vespucci Island</b>.", "Vol.", "OBS", s(76)),
    ("Emperor Sultan", "car", "Berline sport", "port", "Pas d'emplacement fixe : c'est une <b>récompense de Moses</b> après ses missions de livraison de véhicules.", "Terminez la chaîne de Moses (chapitre 2).", "OBS", s(77)),
]

GARAGES = [
    ("Mitchell Auto Center", "4 000 $", "OBS"), ("Persistence Road", "7 600 $ ou 9 500 $ selon les sources", "OBS"),
    ("Vela Rota Drive", "≈ 24 000 à 30 000 $", "OBS"), ("Atlantic Court", "40 000 $ (50 000 $ selon un guide)", "OBS"),
    ("Paradise Garage", "Gratuit avec l'édition Ultimate", "OBS"),
]


def part3(book):
    opener(book, 3, "Véhicules", "Voler, scanner, revendre, stocker : tout sur les véhicules de Leonida, les modèles rares repérés depuis la sortie et un classement provisoire des plus rapides.",
           "night", ["Obtenir un véhicule : vol, achat, récompenses", "Les marques du jeu", "Garages et prix",
                     "Police, armée, air et mer", "Véhicules rares : 11 fiches", "Classement provisoire des plus rapides"], "p3")

    a = book.anchor("p3-base", "Obtenir un véhicule", 2)
    types = "".join(f'<div class="card" style="text-align:center;padding:1.6mm">{vicon(k, c, 70, 34)}<div class="tiny"><b>{n}</b></div><div>{badge(st)}</div></div>'
                    for k, n, c, st in (("car", "Voitures", "#ff7a1a", "CONF"), ("moto", "Motos", "#ff3d6e", "CONF"), ("bike", "Vélos", "#7bd651", "OBS"),
                                        ("boat", "Bateaux", "#38b6ff", "CONF"), ("heli", "Hélicoptères", "#ffd23f", "CONF"), ("plane", "Avions", "#b072ff", "CONF"),
                                        ("airboat", "Hydroglisseurs", "#18d4c4", "CONF"), ("jetski", "Jet-skis", "#ff3d8b", "CONF"), ("suv", "Quads / VTT", "#8d8698", "NC")))
    brands = ["Albany", "Annis", "Ascot", "Benefactor", "Bravado", "Declasse", "Dinka", "Emperor", "Enus", "Grotti", "Karin", "Maibatsu",
              "Nagasaki", "Obey", "Ocelot", "Pegassi", "Pfister", "Progen", "Shitzu", "Truffade", "Vapid"]
    for b in brands:
        book.ix(b, "Marque")
    body = f'''{a}<h2 class="title"><small style="color:#ff7a1a">LES BASES</small>Obtenir un véhicule</h2>
<div class="grid3">{types}</div>
<p class="tiny muted">Les hydroglisseurs et les jet-skis sont confirmés comme activités par Rockstar {s(93)}. La présence de quads et de VTT est signalée, avec moins de certitude {s(83)}.</p>
<h3>Les quatre façons de mettre la main sur un véhicule</h3>
<ul class="small">
<li><b>Le vol</b> : scannez d'abord la voiture avec <b>WAiNK</b> (serrures, alarme, traceur, valeur) {s(87)} {badge("OBS")}.</li>
<li><b>La revente</b> : Moses (Port Gellhorn, chapitre 2) n'accepte que les voitures <b>sans traceur</b>. À partir du chapitre 3, les voitures avec traceur standard se vendent dans n'importe quel <b>Pay 'n' Spray</b> {s(38,39)} {badge("OBS")}.</li>
<li><b>Les récompenses</b> : par exemple l'Emperor Sultan offerte par Moses {s(77)} {badge("OBS")}.</li>
<li><b>Les bonus d'édition</b> : un guide signale une '67 Vapid Dominator Buggy, à récupérer auprès de Wyman avec l'édition Ultimate {s(71)} {badge("NC")}.</li>
</ul>
<h3>Les marques (fictives)</h3>
<p>{"".join(f'<span class="pill">{b}</span>' for b in brands)}</p>
<p class="tiny muted">Aucune marque réelle n'est sous licence. Les équivalents réels cités sur Internet sont des identifications de fans {s(84,83)} {badge("OBS")}. Le nombre total de modèles varie de 185 à 324 selon les bases de données. Pour le 100 %, les guides parlent de <b>200 scans sur 277 modèles de base</b> {s(27)}.</p>'''
    book.add(3, body)

    a = book.anchor("p3-garages", "Garages et prix", 2)
    rows = "".join(f'<tr><td><b>{book.ix(n, "Lieu")}</b></td><td>{p}</td><td>{badge(st)}</td></tr>' for n, p, st in GARAGES)
    body = f'''{a}<h2 class="title"><small style="color:#ff7a1a">STOCKER SA COLLECTION</small>Garages</h2>
<div class="ill" style="height:26mm;margin-bottom:2mm">{scene("night", 420, 100)}</div>
<p class="small">Selon les guides, il y a <b>8 garages à acheter</b> via l'application <b>Vice City Real Estate</b>, pour environ <b>160 000 $</b> au total {s(71,72,73)} {badge("OBS")}. La carte interactive de GTABase recense 14 emplacements de garages, en comptant ceux qui sont fournis par l'histoire ou par les éditions {s(74)}.</p>
<table class="t" style="--acc:#ff7a1a"><tr><th>Garage</th><th>Prix signalé</th><th>Statut</th></tr>{rows}</table>
<p class="tiny muted">Les prix diffèrent selon les guides (voir la colonne). Vérifiez dans l'application avant d'acheter. Les trois garages restants n'ont pas de prix recoupé à ce jour.</p>
{tip("Le trophée « <b>Little Boxes</b> » est associé à l'achat des garages selon Game Rant {s}. Commencez par le moins cher (Mitchell Auto Center) pour mettre vos premières voitures rares à l'abri.".replace("{s}", s(73)), "Trophée", "gold", "🏆")}'''
    book.add(3, body)

    a = book.anchor("p3-cat", "Police, armée, air et mer", 2)
    def vrow(kind, col, name, desc, st, src):
        book.ix(name, "Véhicule")
        return (f'<div class="card" style="display:flex;gap:2mm;align-items:center;padding:1.6mm 2.2mm">{vicon(kind, col, 58, 28)}'
                f'<div style="flex:1"><div class="ctitle"><h4 style="font-size:8pt">{name}</h4>{badge(st)}</div><div class="tiny">{desc}</div>'
                f'<div class="src">{src}</div></div></div>')
    body = f'''{a}<h2 class="title"><small style="color:#ff7a1a">FLOTTES SPÉCIALES</small>Police, armée, air &amp; mer</h2>
<div class="grid2">
<div><h3 style="margin-top:0">🚓 Police</h3>
{vrow("police", "#38b6ff", "Police Cruiser (base Buffalo)", "Voiture de patrouille, citée par plusieurs listes.", "OBS", s(97,83))}
{vrow("police", "#38b6ff", "Gauntlet Interceptor", "Muscle car de police.", "NC", s(97))}
{vrow("truck", "#38b6ff", "Police Riot", "Véhicule blindé anti-émeute.", "NC", s(97))}
{vrow("heli", "#38b6ff", "Police Maverick", "Hélicoptère de poursuite, le plus souvent cité.", "OBS", s(97,83))}
{vrow("boat", "#38b6ff", "Bateaux de police", "Les noms diffèrent selon les sources (Dingus Police Como, Police Garda, Rugger Police Rhode…).", "NC", s(97,84))}
</div><div><h3 style="margin-top:0">🪖 Armée et engins lourds</h3>
{vrow("tank", "#7bd651", "Rhino (char)", "Char de combat, cité comme véhicule militaire.", "NC", s(84,83))}
{vrow("heli", "#7bd651", "Cargobob", "Hélicoptère de transport lourd.", "NC", s(84))}
{vrow("heli", "#7bd651", "Valkyrie", "Hélicoptère militaire.", "NC", s(84))}
<h3>✈️ Air et 🌊 mer</h3>
{vrow("heli", "#ffd23f", "Sea Sparrow", "Hélicoptère léger à flotteurs, pour se poser sur l'eau.", "NC", s(84))}
{vrow("airboat", "#18d4c4", "Hydroglisseur", "L'activité « air boating » est confirmée. Il est idéal pour Grassrivers.", "CONF", s(93))}
</div></div>
<p class="tiny muted">Ces catégories reposent surtout sur des bases de fans. Les chiffres varient (de 34 à 47 véhicules de service selon les sources). Une fiche détaillée par modèle viendra avec les mises à jour.</p>'''
    book.add(3, body)

    # Rare vehicles : 2 pages
    for part_i, chunk in enumerate((RARE[:4], RARE[4:8], RARE[8:])):
        aid = "p3-rares" if part_i == 0 else f"p3-rares{part_i+1}"
        a = book.anchor(aid, "Véhicules rares (fiches)" if part_i == 0 else None, 2)
        cards = ""
        for name, kind, cat, reg, loc, how, st, src in chunk:
            book.ix(name, "Véhicule")
            mini = (f'<div class="mapbox" style="width:24mm;flex:0 0 24mm">{leonida_map(highlight=[reg], markers=[(reg, "★", "#ffd23f")], show_labels=False, title=False)}</div>'
                    if reg else '<div class="mapbox" style="width:24mm;flex:0 0 24mm;display:flex;align-items:center;justify-content:center;text-align:center;font-size:5.6pt;color:#9fd9e0;padding:1mm">Région non précisée par les sources</div>')
            cards += (f'<div class="card accent" style="--acc:#ffd23f;display:flex;gap:2.4mm;padding:2mm 2.4mm">'
                      f'<div style="flex:0 0 22mm;text-align:center">{vicon(kind, "#ffb020", 84, 40)}<div class="tiny muted">{cat}</div></div>'
                      f'<div style="flex:1"><div class="ctitle"><h4>{name}</h4>{badge(st)}</div>'
                      f'{kv([("Où", loc), ("Comment", how), ("Achat", "Non documenté")])}'
                      f'<div class="src">Sources : {src} · {yt("GTA 6 " + name + " location")}</div></div>{mini}</div>')
        title = (f'<h2 class="title"><small style="color:#ffd23f">CHASSE AUX PÉPITES</small>Véhicules rares</h2>'
                 f'<p class="small">Emplacements relevés par les guides depuis la sortie. Certaines apparitions dépendent de l\'heure. '
                 f'Une source précise : « signalé, non testé par nous ». Allez-y avec deux sources ouvertes.</p>') if part_i == 0 else \
                f'<h2 class="title"><small style="color:#ffd23f">SUITE</small>Véhicules rares</h2>'
        book.add(3, f'{a}{title}{cards}')

    a = book.anchor("p3-top", "Classement : les plus rapides", 2)
    top = [("Truffade Thrax", "8,7 / 10", "Note de vitesse d'origine la plus élevée (supersportive)", "OBS"),
           ("Truffade Thrax modifiée (Andrew Node)", "9,2 / 10", "Version modifiée signalée par un guide", "NC"),
           ("Progen Emerus", "8,3 / 10", "", "OBS"), ("Pegassi Vitello", "8,2 / 10", "Voir la fiche « rares »", "OBS"),
           ("Grotti Itali RSX", "≈ 217 km/h (estimation)", "Classée première par un autre guide, sur la vitesse estimée", "NC")]
    for t in top:
        book.ix(t[0].split(" (")[0], "Véhicule")
    rows = "".join(f'<tr><td style="font-family:Inter Display;font-weight:900;color:#ffd23f;font-size:11pt">{i+1}</td><td><b>{n}</b><div class="tiny muted">{c}</div></td><td>{v}</td><td>{badge(st)}</td></tr>'
                   for i, (n, v, c, st) in enumerate(top))
    body = f'''{a}<h2 class="title"><small style="color:#ff7a1a">CLASSEMENT PROVISOIRE</small>Les plus rapides</h2>
<div style="display:flex;justify-content:center;margin:1mm 0 2mm">{vicon("super", "#ff3d6e", 220, 106)}</div>
<table class="t" style="--acc:#ffd23f"><tr><th>#</th><th>Véhicule</th><th>Valeur</th><th>Statut</th></tr>{rows}</table>
{tip("Au 21 novembre 2026, <b>aucune vitesse de pointe mesurée</b> en jeu n'avait été publiée {s}. Ce classement repose sur la note de vitesse affichée par le jeu. Il sera remplacé par des mesures dès qu'elles seront disponibles.".replace("{s}", s(81)), "Pourquoi provisoire ?", "warn", "⏱️")}
<p class="src">Sources : {s(79,80,81)}</p>
<h3>Les autres classements</h3>
<p class="small">Les classements « meilleur tout-terrain », « meilleure moto », « meilleur bateau » et « meilleur hélicoptère » seront publiés dans une mise à jour, quand des tests comparables seront disponibles. Nous ne publions pas de classement inventé.</p>'''
    book.add(3, body)


# ---------------------------------------------------------------------------
# PARTIE 4 — ANIMAUX
# ---------------------------------------------------------------------------
ANIMALS = [
    # (nom, emoji, catégorie, habitat, régions, note jeu, statut, sources)
    ("Alligator", "🐊", "Reptile", "Marais, canaux", ["grass"], "Très présent dans les marais de Grassrivers. Il apparaît dans les bandes-annonces officielles.", "CONF", (57, 58, 61)),
    ("Crocodile", "🐊", "Reptile", "Côtes, eaux saumâtres", ["keys"], "Cité parmi les espèces montrées.", "OBS", (60,)),
    ("Flamant rose", "🦩", "Oiseau", "Lagunes, Vice City", ["vice"], "Aperçu autour de Vice City, notamment près de la piscine d'un hôtel.", "CONF", (57, 58, 61)),
    ("Pélican", "🐦", "Oiseau", "Littoral, pontons", ["keys", "vice"], "Espèce montrée dans les bandes-annonces.", "CONF", (58,)),
    ("Lamantin", "🌊", "Mammifère marin", "Eaux côtières calmes", ["keys"], "Espèce montrée dans les bandes-annonces (pictogramme générique).", "CONF", (58,)),
    ("Goéland", "🐦", "Oiseau", "Plages", ["vice"], "Fréquent autour de Vice City.", "OBS", (61,)),
    ("Dauphin", "🐬", "Mammifère marin", "Large", ["keys"], "Cité parmi les espèces montrées.", "OBS", (60,)),
    ("Requin", "🦈", "Poisson", "Large", ["keys"], "Cité parmi les espèces montrées.", "OBS", (60,)),
    ("Tortue de mer", "🐢", "Reptile marin", "Littoral, récifs", ["keys"], "Citée parmi les espèces montrées.", "OBS", (60,)),
    ("Cougar (puma)", "🐆", "Mammifère", "Forêts, collines", ["kalaga"], "Signalé dans Mount Kalaga National Park.", "OBS", (60, 62)),
    ("Cerf", "🦌", "Mammifère", "Forêts, prairies", ["kalaga"], "Signalé dans Mount Kalaga National Park.", "OBS", (60, 62)),
    ("Ours noir", "🐻", "Mammifère", "Forêts", ["kalaga"], "Présent dans la liste des espèces terrestres.", "OBS", (63,)),
    ("Sanglier", "🐗", "Mammifère", "Bois, campagne", ["kalaga", "ambrosia"], "Présent dans la liste des espèces terrestres.", "OBS", (63,)),
    ("Lynx roux", "🐈", "Mammifère", "Bois, broussailles", ["kalaga"], "Présent dans la liste des espèces terrestres.", "OBS", (63,)),
    ("Castor", "🦫", "Mammifère", "Rivières", ["kalaga"], "Présent dans la liste des espèces terrestres.", "OBS", (63,)),
    ("Crapaud buffle", "🐸", "Amphibien (invasif)", "Jardins, zones humides", ["grass", "vice"], "Classé parmi les espèces invasives.", "OBS", (59, 63)),
    ("Iguane vert", "🦎", "Reptile (invasif)", "Zones urbaines et côtières", ["vice", "keys"], "Classé parmi les espèces invasives.", "OBS", (59,)),
    ("Macaque rhésus", "🐒", "Primate (invasif)", "Bois", [], "Classé parmi les espèces invasives. Zone non précisée.", "OBS", (59,)),
    ("Chat (haret)", "🐈", "Mammifère (invasif)", "Partout", [], "Chats harets classés invasifs. Les chats domestiques existent aussi.", "OBS", (59, 63)),
    ("Serpents", "🐍", "Reptile", "Marais ; animaux de compagnie", ["grass"], "Des serpents de compagnie sont présents dans le jeu.", "OBS", (64,)),
    ("Chien", "🐕", "Mammifère", "Partout", [], "Compagnon courant. Voir aussi le « Cool Dog » en jet-ski (Partie 6).", "OBS", (64, 52)),
    ("Poissons (≈ 35 espèces)", "🐟", "Poissons", "Mer, lacs, marais", ["keys", "grass", "kalaga"], "Pêche en « capture et relâche ». Candy Fish signalé à Grassrivers.", "OBS", (58, 65)),
]


def part4(book):
    opener(book, 4, "Animaux", "Une encyclopédie de la faune de Leonida : où observer chaque espèce, comment l'étudier pour votre journal, et les bases de la pêche et de la chasse.",
           "grass", ["Le journal de la faune : comment étudier", "Carte des habitats", "Fiches espèces (22 entrées)", "Pêche et chasse"], "p4")

    a = book.anchor("p4-journal", "Le journal de la faune", 2)
    body = f'''{a}<h2 class="title"><small style="color:#7bd651">OBSERVER &amp; ÉTUDIER</small>Le journal de la faune</h2>
<div class="ill" style="height:30mm;margin-bottom:2mm">{scene("kalaga", 420, 110)}</div>
<div class="grid2">
{card("Combien d'espèces ?", '<p class="small">Le chiffre de <b>plus de 170 espèces</b> circule depuis la présentation du jeu. Le <b>journal</b> compterait <b>255 entrées</b>, les races étant comptées séparément. Les deux chiffres ne mesurent pas la même chose.</p>', "OBS", s(58,59), "#7bd651", "📖")}
{card("Pour le 100 %", '<p class="small">Il faut étudier <b>100 animaux sur 255</b>. La chasse n\'est pas obligatoire pour le 100 %.</p>', "OBS", s(27), "#ffd23f", "✅")}
</div>
<h3>Comment étudier un animal</h3>
<ol class="small" style="padding-left:4.5mm">
<li>Regardez l'animal avec des <b>jumelles</b> ou une <b>lunette</b> {s(59)}.</li>
<li>Un guide indique les commandes suivantes : maintenir <b>L2 / LT</b> pour viser, puis maintenir <b>R1 / RB</b> à l'invite pour étudier {s(62)} {badge("NC")}.</li>
<li>L'espèce s'ajoute alors à votre journal.</li>
</ol>
{tip("Un guide signale qu'une fois un animal amical enregistré, on peut le <b>caresser</b> {s}. Approchez lentement les animaux sauvages : leur comportement exact en jeu reste peu documenté.".replace("{s}", s(62)), "Bon à savoir", "", "🐾")}'''
    book.add(4, body)

    a = book.anchor("p4-hab", "Carte des habitats", 2)
    hab = [("grass", "🐊", "Marais : alligators, serpents, crapauds"), ("keys", "🐬", "Mer et îles : dauphins, requins, tortues, lamantins, pélicans"),
           ("vice", "🦩", "Ville et plages : flamants, goélands, iguanes"), ("kalaga", "🦌", "Parc national : cerfs, cougars, ours, castors"),
           ("ambrosia", "🐗", "Campagne : sangliers (signalés)"), ("port", "🐦", "Côte du golfe : oiseaux marins (à documenter)")]
    mk = [(k, str(i + 1), "#7bd651") for i, (k, _, _) in enumerate(hab)]
    leg = "".join(f'<div class="cbrow" style="border-bottom:.25mm dotted rgba(255,255,255,.15)"><b style="color:#7bd651;width:4mm">{i+1}</b><span class="emoji" style="font-size:11pt">{e}</span><span class="small">{t}</span></div>'
                  for i, (k, e, t) in enumerate(hab)).replace('class="cbrow"', 'style="display:flex;gap:1.6mm;padding:.8mm 0"')
    body = f'''{a}<h2 class="title"><small style="color:#7bd651">OÙ CHERCHER</small>Carte des habitats</h2>
<div class="mapbox" style="width:72%;margin:0 auto">{leonida_map(markers=mk)}</div>
<div style="margin-top:2mm">{leg}</div>
<p class="tiny muted">Habitats déduits des régions citées par les sources {s(57,61,62)}. Ce sont des zones de présence probable, pas des points d'apparition garantis.</p>'''
    book.add(4, body)

    per_page = 6
    for pi in range(0, len(ANIMALS), per_page):
        chunk = ANIMALS[pi:pi + per_page]
        a = book.anchor("p4-especes" if pi == 0 else f"p4-especes{pi}", "Fiches espèces" if pi == 0 else None, 2)
        cards = ""
        for name, emo, cat, habitat, regs, note, st, src in chunk:
            book.ix(name, "Animal")
            mini = leonida_map(highlight=regs, show_labels=False, title=False) if regs else ""
            mbox = (f'<div class="mapbox" style="width:17mm;flex:0 0 17mm">{mini}</div>' if regs else
                    '<div class="mapbox" style="width:17mm;flex:0 0 17mm;font-size:5.2pt;color:#9fd9e0;display:flex;align-items:center;text-align:center;padding:.6mm">Zone non précisée</div>')
            cards += (f'<div class="card accent" style="--acc:#7bd651;display:flex;gap:2mm;padding:1.8mm 2.2mm;margin-bottom:1.6mm">'
                      f'<div class="emoji" style="font-size:20pt;flex:0 0 11mm;text-align:center;line-height:1.2">{emo}</div>'
                      f'<div style="flex:1"><div class="ctitle"><h4 style="font-size:8.6pt">{name}</h4>{badge(st)}</div>'
                      f'<div class="tiny"><b style="color:#7bd651">{cat}</b> · {habitat}</div><div class="tiny">{note}</div>'
                      f'<div class="src">Sources : {s(*src)}</div></div>{mbox}</div>')
        head = (f'<h2 class="title"><small style="color:#7bd651">ENCYCLOPÉDIE</small>Fiches espèces</h2>' if pi == 0 else
                f'<h2 class="title"><small style="color:#7bd651">ENCYCLOPÉDIE (SUITE)</small>Fiches espèces</h2>')
        book.add(4, f'{a}{head}{cards}<p class="tiny muted">Pictogrammes génériques (police Noto Emoji, licence libre), pas des représentations du jeu.</p>')

    a = book.anchor("p4-peche", "Pêche et chasse", 2)
    body = f'''{a}<h2 class="title"><small style="color:#7bd651">ACTIVITÉS NATURE</small>Pêche &amp; chasse</h2>
<div class="ill" style="height:26mm;margin-bottom:2mm">{scene("sea", 420, 100)}</div>
<div class="grid2"><div>
<h3 style="margin-top:0">🎣 Pêche</h3>
<ul class="small">
<li><b>La canne</b> est gratuite : sur le ponton derrière la maison de Jason à Key Lento, et dans l'onglet Équipement de la roue d'armes {s(65,67)} {badge("OBS")}.</li>
<li><b>Le leurre de départ</b> : la canne est fournie avec un Small Saltwater Lure, adapté aux petits poissons {s(65)}.</li>
<li><b>Repérer les poissons</b> : passez en mode Focus (L3 + R3) pour voir les zones les plus poissonneuses. Les poissons apparaissent comme des taches pâles lumineuses {s(65,66)} {badge("OBS")}.</li>
<li><b>Capture et relâche</b> : les poissons ne se vendent pas {s(65)}.</li>
<li>Selon un guide, la pêche fait progresser la statistique Focus {s(59)} {badge("NC")}.</li>
</ul></div><div>
{card("Défi de Cal : « Catch a Bigger Fish »", '<p class="small">Rendez-vous en bateau au <b>spot de pêche violet de Gambit Bay</b>.</p>', "OBS", s(65,42), "#18d4c4", "🐟")}
<h3>🦌 Chasse</h3>
<p class="small">La chasse est liée à la quête de <b>Bret Vogel</b> (chapitre 2), qui paie à l'animal {s(59,41)} {badge("OBS")}. Elle n'est pas nécessaire pour étudier les animaux du journal {s(27)}.</p>
</div></div>
<p class="tiny muted">Repères cités pour la pêche : Candy Fish à Grassrivers (nord du comté de Mariana), Salt Fish à Buckskin Swamp (ouest de Vice-Dale) {badge("NC")}. Le nombre de spots, de leurres et de poissons légendaires n'est pas encore documenté de façon fiable.</p>'''
    book.add(4, body)


# ---------------------------------------------------------------------------
# PARTIE 5 — MISSIONS & ACTIVITÉS
# ---------------------------------------------------------------------------
CHAPTERS = [
    ("Prologue", "—", "Introduction de l'histoire"),
    ("Chapitre 1 — « Just Like Paradise »", "Leonida Keys", "22 à 24 missions principales selon les sources, plus des missions optionnelles"),
    ("Chapitre 2 — « Paradise Lost »", "Port Gellhorn", "Débloque Moses, Kyle, Bret Vogel et Billy"),
    ("Chapitre 3 — « Tits, Ass, Drug Money »", "Vice City", "Débloque Yago et Yasmani, les receleurs et le Pay 'n' Spray"),
    ("Chapitre 4 — « Vice City, Baby »", "Vice City", "Pilot Pete, puis les coffres-forts en fin de chapitre"),
    ("Chapitre 5 — « Top of the World, Ma »", "Vice City et Leonida", "Mission finale : « The End of the Road »"),
]

CH1 = ["Gone Fishing", "Gear Up", "Lab Fees", "Just a Scratch", "Unwanted Attention", "Pipework", "Hey Arnold!", "Island Dreams",
       "Feng Shui", "Coming Home", "Buck Me", "Down to Earth", "Swamped", "Don Gone", "Recalibration", "Tourist Trap",
       "Home Sweet Home", "Discharge Time"]

SF = [
    ("1", "Kirk", "La chasse au Skunk Ape", "Compte pour le trophée", "OBS"),
    ("1", "Shirley", "Livraisons de rhum et de scooters", "Ne compterait pas pour le trophée (sources en désaccord)", "OBS"),
    ("1", "Kenton", "Plongées au trésor (épaves)", "Lié aux « shipwreck sets »", "OBS"),
    ("1", "Cal", "Défi de pêche « Catch a Bigger Fish »", "Spot violet de Gambit Bay", "OBS"),
    ("2", "Kyle", "Épandage agricole et travaux de ferme", "Compte pour le trophée", "OBS"),
    ("2", "Moses", "Vols de voitures (répétables)", "Récompense : Emperor Sultan", "OBS"),
    ("2", "Bret Vogel", "Missions de chasse", "Paie à l'animal", "OBS"),
    ("2", "Billy", "Événements du Thrillbilly Mud Club", "Trophée à part (sources en désaccord)", "OBS"),
    ("3", "Yago", "Chaîne de courses de rue", "⏳ Limitée dans le temps : à faire en priorité", "OBS"),
    ("3", "Yasmani", "Braquages de bijouteries, de distributeurs et de prêteurs sur gages", "Rapporte bien, ne compte pas pour le trophée", "OBS"),
    ("4", "Pilot Pete", "Missions « Last Mile » et vols de livraison", "Compte pour le trophée", "OBS"),
]


def part5(book):
    opener(book, 5, "Missions & activités", "La structure de l'histoire, les quêtes « Strangers & Freaks », les opérations illégales, les braquages et toutes les activités confirmées.",
           "port", ["Structure de l'histoire (⚠ spoilers)", "Missions du chapitre 1", "Strangers & Freaks : les quêtes",
                    "Opérations illégales, braquages et receleurs", "Activités et loisirs"], "p5")

    a = book.anchor("p5-histoire", "Structure de l'histoire", 2)
    rows = "".join(f'<tr><td><b>{c}</b></td><td>{r}</td><td class="tiny">{n}</td></tr>' for c, r, n in CHAPTERS)
    body = f'''{a}<h2 class="title"><small style="color:#ffd23f">CAMPAGNE</small>Structure de l'histoire</h2>
<p>{badge("SPOIL")} {badge("OBS")}</p>
<p class="small">La campagne compte un <b>prologue suivi de 5 chapitres</b> et un peu plus de 90 missions principales {s(10,45,46,47,100)}. Certaines missions se jouent avec un seul des héros, d'autres avec les deux {s(12)}.</p>
<table class="t" style="--acc:#ffd23f"><tr><th>Chapitre</th><th>Région</th><th>À noter</th></tr>{rows}</table>
{tip("Le contenu secondaire se débloque <b>chapitre par chapitre</b>. Comme certaines quêtes sont limitées dans le temps, faites le tour des activités avant chaque mission qui fait avancer l'histoire de façon importante.", "Stratégie", "gold", "🧭")}
<p class="tiny muted">Les guides ne comptent pas les missions de la même façon (par exemple 22 ou 24 au chapitre 1). Les fiches détaillées de chaque mission (objectif, déroulement, récompenses) seront publiées au fil des mises à jour : nous ne publions pas de déroulés non vérifiés.</p>'''
    book.add(5, body)

    a = book.anchor("p5-ch1", "Missions du chapitre 1", 2)
    notes = {"Buck Me": "Débloque l'application bancaire BuckMe", "Island Dreams": "Débloque les découvertes sous-marines",
             "Gone Fishing": "Première mission du chapitre après le prologue"}
    rows = "".join(f'<tr><td style="color:#ffd23f;font-weight:800">{i+1:02d}</td><td><b>{book.ix(m, "Mission")}</b></td><td class="tiny">{notes.get(m, "")}</td></tr>' for i, m in enumerate(CH1))
    body = f'''{a}<h2 class="title"><small style="color:#ffd23f">CHAPITRE 1 · LEONIDA KEYS</small>« Just Like Paradise »</h2>
<p>{badge("SPOIL")} {badge("OBS")}</p>
<table class="t" style="--acc:#ffd23f"><tr><th>#</th><th>Mission</th><th>Ce qu'elle débloque</th></tr>{rows}</table>
<p class="tiny muted">Liste reprise des guides de soluce {s(45,46,47)}. L'ordre peut varier, et quelques missions comptées par certains guides manquent ici (de 22 à 24 missions au total selon les sources).</p>
{tip("Avant la fin du chapitre, terminez les quêtes de Kirk, Shirley, Kenton et Cal, et revendez vos stupéfiants à <b>Donnie</b>. D'après un guide, ce receleur n'est disponible qu'au chapitre 1, au sud de Key Lento {s}.".replace("{s}", s(38)), "Avant de quitter les Keys", "warn", "⛔")}'''
    book.add(5, body)

    a = book.anchor("p5-sf", "Strangers & Freaks", 2)
    rows = "".join(f'<tr><td style="color:#ffd23f;font-weight:900">{c}</td><td><b>{n}</b></td><td>{q}</td><td class="tiny">{r}</td></tr>' for c, n, q, r, st in SF)
    body = f'''{a}<h2 class="title"><small style="color:#ffd23f">QUÊTES SECONDAIRES</small>Strangers &amp; Freaks</h2>
<p class="small">Ce sont des chaînes de missions en plusieurs épisodes, proposées par des personnages hauts en couleur de tout Leonida. Terminer <b>8 chaînes éligibles</b> rapporte un trophée Argent {s(44)} {badge("OBS")}.</p>
<table class="t" style="--acc:#ffd23f"><tr><th>Ch.</th><th>Contact</th><th>Quête</th><th>À noter</th></tr>{rows}</table>
<p class="src">Sources : {s(40,41,42,43,44)}. Les sources ne s'accordent pas sur les quêtes de Billy et de Shirley pour le trophée. Les chaînes de Kirk, Kyle, Yago et Pilot Pete sont les plus souvent citées comme éligibles.</p>'''
    book.add(5, body)

    a = book.anchor("p5-illegal", "Opérations illégales, braquages et receleurs", 2)
    body = f'''{a}<h2 class="title"><small style="color:#ffd23f">CRIME ORGANISÉ</small>Opérations &amp; braquages</h2>
<div class="grid2">
{card("Opérations illégales (Illegal Operations)", '<ul class="small"><li><b>39</b> opérations réparties entre <b>9 gangs</b>, signalées par des icônes jaunes.</li><li>Certaines n\'apparaissent sur la carte qu\'une fois sur place, d\'autres à partir d\'un indice (dialogue, note avec un code de coffre).</li><li>Survolez l\'icône sur la carte pour voir les objets de valeur à récupérer.</li><li>Elles se réapprovisionnent avec le temps.</li><li>Trophée <b>Pest Control</b> : braquer une opération par gang.</li></ul>', "OBS", s(37,39,12), "#ffd23f", "🏴")}
{card("Coffres-forts (vaults)", '<ul class="small"><li>Ils se débloquent avec la mission optionnelle de Yasmani <b>« That\'s Where The Money Is… »</b>, en fin de chapitre 4.</li><li>Un braquage de coffre déclenche <b>4 étoiles</b>.</li><li>Il en faut <b>8 sur 8</b> pour le 100 %.</li></ul>', "OBS", s(39,28,22), "#e5243b", "🏦")}
{card("Receleurs (fences)", '<ul class="small"><li><b>Donnie</b> : chapitre 1 uniquement, au sud de Key Lento. Il achète les stupéfiants à bas prix.</li><li><b>Moses</b> : Port Gellhorn, à partir du chapitre 2. Il prend les voitures sans traceur.</li><li><b>Pay \'n\' Spray</b> : à partir du chapitre 3, pour les voitures avec traceur standard.</li></ul>', "OBS", s(38,39), "#b072ff", "💰")}
{card("Objectifs de recel (100 %)", '<ul class="small"><li>Stupéfiants : 100 000 $</li><li>Bijoux : 100 000 $</li><li>Billets marqués : 250 000 $</li><li>Véhicules : 200 000 $</li></ul>', "OBS", s(28), "#38b6ff", "🎯")}
</div>
{tip("Un guide indique que les opérations illégales attirent <b>moins de Heat</b> que les braquages de magasins, de banques ou de bijouteries {s}.".replace("{s}", s(39)), "À tester", "", "🧪")}'''
    book.add(5, body)

    a = book.anchor("p5-activites", "Activités et loisirs", 2)
    conf = ["Hydroglisseur", "Saut en parachute (base jump)", "Billard", "Salle de sport", "Jet-ski", "Mini-golf", "Plongée sous-marine", "Snorkeling",
            "Courses de rue", "Courses tout-terrain", "Zoos", "Kayak", "Parachutisme", "Pêche"]
    obs = [("Thrillbilly Mud Club (Billy)", s(41)), ("Défis de course (médailles d'or)", s(31,32)), ("Cascades / sauts", s(33)),
           ("Contre-la-montre en drone", s(29)), ("Paniers de basket (100)", s(30)), ("Spots de méditation (18)", s(35,36)),
           ("Chasse (Bret Vogel)", s(41)), ("Vols de livraison (Pilot Pete)", s(42))]
    for c in conf:
        book.ix(c, "Activité")
    body = f'''{a}<h2 class="title"><small style="color:#ffd23f">TEMPS LIBRE</small>Activités</h2>
<div class="ill" style="height:24mm;margin-bottom:2mm">{scene("keys", 420, 90)}</div>
<h3>Confirmées par Rockstar ou montrées officiellement {badge("CONF")}</h3>
<p>{"".join(f'<span class="pill">✔ {c}</span>' for c in conf)}</p>
<p class="src">Sources : {s(93)} (liste confirmée via Game Informer et les vidéos officielles).</p>
<h3>Observées depuis la sortie {badge("OBS")}</h3>
<table class="t" style="--acc:#ffd23f"><tr><th>Activité</th><th>Sources</th></tr>{"".join(f"<tr><td>{n}</td><td>{sr}</td></tr>" for n, sr in obs)}</table>
<p class="tiny muted">Les événements aléatoires et les défis spéciaux ne sont pas encore recensés de façon fiable. Ils seront ajoutés à la rubrique « Dernières découvertes ».</p>'''
    book.add(5, body)
