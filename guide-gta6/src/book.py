# -*- coding: utf-8 -*-
"""Moteur de mise en page : pages fixes A5, en-têtes/pieds, navigation,
sommaire et index générés automatiquement."""

from lib import CSS, PART_COLORS, E

PART_NAMES = {
    0: "Guide GTA VI", 1: "Partie 1 · Bien démarrer", 2: "Partie 2 · Carte & lieux",
    3: "Partie 3 · Véhicules", 4: "Partie 4 · Animaux", 5: "Partie 5 · Missions & activités",
    6: "Partie 6 · Easter Eggs & secrets", 7: "Partie 7 · Astuces & techniques",
    8: "Partie 8 · Collectibles", 9: "Partie 9 · Checklist 100 %", 10: "Partie 10 · Le meilleur",
}


class Book:
    def __init__(self):
        self.pages = []          # html des pages
        self.toc = []            # (level, label, anchor)
        self.index = []          # (term, category, page)
        self.anchor_page = {}

    @property
    def next_no(self):
        return len(self.pages) + 1

    def anchor(self, aid, label=None, level=None):
        self.anchor_page[aid] = self.next_no
        if label:
            self.toc.append((level or 2, label, aid))
        return f'<span id="{aid}" class="sec-id"></span>'

    def ix(self, term, cat):
        """Enregistre un terme d'index pour la page en cours, renvoie le terme."""
        self.index.append((term, cat, self.next_no))
        return term

    def add(self, part, body, bg="", chrome=True, raw=False, slot=None):
        no = (slot + 1) if slot is not None else self.next_no
        out = self.pages if slot is None else []
        col = PART_COLORS.get(part, "#ff7a1a")
        if raw:
            out.append(f'<section class="page" id="pg-{no}" style="--acc:{col}">{bg}{body}</section>')
            if slot is not None: self.pages[slot] = out[0]
            return
        hdr = ftr = ""
        if chrome:
            hdr = (f'<div class="hdr"><span class="part" style="color:{col}">{E(PART_NAMES.get(part, ""))}</span>'
                   f'<span class="nav"><a href="#sommaire">☰ Sommaire</a><a href="#carte">◎ Carte</a>'
                   f'<a href="#check">☑ 100 %</a><a href="#index">A–Z</a></span></div>')
            ftr = (f'<div class="ftr"><span>GTA VI · Le Guide Ultime — Édition Premium · v1.0</span>'
                   f'<span class="num" style="color:{col}">{no:02d}</span></div>')
        deco = bg or (f'<svg class="bgdeco" viewBox="0 0 148 210" preserveAspectRatio="none">'
                      f'<defs><radialGradient id="rg{no}" cx="1" cy="0" r="1"><stop offset="0" stop-color="{col}" stop-opacity=".22"/>'
                      f'<stop offset=".6" stop-color="{col}" stop-opacity="0"/></radialGradient></defs>'
                      f'<rect width="148" height="210" fill="url(#rg{no})"/>'
                      f'<rect x="0" y="0" width="1.6" height="210" fill="{col}"/></svg>')
        out.append(f'<section class="page" id="pg-{no}" style="--acc:{col}">{deco}{hdr}'
                          f'<div class="content">{body}</div>{ftr}</section>')
        if slot is not None:
            self.pages[slot] = out[0]

    def placeholder(self, key):
        """Réserve une page dont le contenu sera calculé à la fin (sommaire)."""
        self.pages.append(f"@@{key}@@")
        return len(self.pages) - 1

    def fill(self, key, html):
        for i, p in enumerate(self.pages):
            if p == f"@@{key}@@":
                self.pages[i] = html
                return
        raise KeyError(key)

    def html(self):
        return ('<!doctype html><html lang="fr"><head><meta charset="utf-8">'
                '<title>GTA VI — Le Guide Ultime (Édition Premium)</title>'
                f'<style>{CSS}</style></head><body>' + "\n".join(self.pages) + '</body></html>')
