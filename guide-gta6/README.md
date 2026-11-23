# GTA VI — Le Guide Ultime (Édition Premium) · v1.0

Guide francophone **non officiel** de Grand Theft Auto VI : un PDF interactif de 80 pages au format A5, lisible sur smartphone.

**Livrable :** `dist/GTA-VI-Le-Guide-Ultime-Edition-Premium-v1.0.pdf`

## Contenu
- 10 parties : démarrage, carte et régions, véhicules, faune, missions et activités, Easter Eggs, astuces, collectibles, checklist 100 %, best-of.
- Chaque information porte un statut **Confirmé / Observé / Non confirmé** et renvoie à l'une des 100 sources numérotées, datées et cliquables.
- Sommaire cliquable, bookmarks PDF, navigation en en-tête, index A–Z et 109 cases à cocher (AcroForm).
- Toutes les illustrations sont des créations originales en SVG. Aucune capture du jeu. Les cartes sont des schémas de repérage non à l'échelle.

## Régénérer le PDF
```bash
python3 src/build.py      # contenu -> build/guide.html (+ toc.json)
node src/render.cjs       # Chromium/Playwright -> build/guide-raw.pdf (+ contrôle des débordements)
python3 src/add_forms.py  # cases à cocher + signets + métadonnées -> dist/
```
Prérequis : Python 3 avec reportlab et pypdf, Node avec playwright (Chromium), les polices Inter et Noto Color Emoji.

## Mettre à jour
- Le contenu est dans `src/content_a.py` à `src/content_d.py`, les sources dans `src/sources.py`.
- Ajoutez chaque nouveauté avec son statut et ses sources, puis notez-la dans le journal « Dernières découvertes » (`content_d.latest`).
- `render.cjs` signale toute page qui déborde (`OVERFLOW`).
