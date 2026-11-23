# -*- coding: utf-8 -*-
"""Ajoute de vraies cases à cocher (AcroForm) au PDF rendu par Chromium."""
import json, os, re
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import Color, transparent
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, ArrayObject, DictionaryObject

root = os.path.join(os.path.dirname(__file__), "..")
raw = os.path.join(root, "build", "guide-raw.pdf")
boxes = json.load(open(os.path.join(root, "build", "checkboxes.json")))
reader = PdfReader(raw)
n = len(reader.pages)
W, H = 148 * mm, 210 * mm

ov = os.path.join(root, "build", "overlay.pdf")
c = canvas.Canvas(ov, pagesize=(W, H))
by_page = {}
for b in boxes:
    by_page.setdefault(b["page"], []).append(b)
for i in range(n):
    for b in by_page.get(i, []):
        name = re.sub(r"[^A-Za-z0-9_]", "_", b["name"])[:60]
        size = b["w"] * mm
        c.acroForm.checkbox(name=name, tooltip="Cocher", x=b["x"] * mm, y=H - (b["y"] + b["h"]) * mm, size=size,
                            buttonStyle="check", borderWidth=0, borderColor=transparent,
                            fillColor=transparent, textColor=Color(1, 0.82, 0.25), forceBorder=False)
    c.showPage()
c.save()

writer = PdfWriter(clone_from=raw)
ovr = PdfReader(ov)
fields = ArrayObject()
for i, page in enumerate(writer.pages):
    op = ovr.pages[i]
    if "/Annots" not in op:
        continue
    annots = page.get("/Annots")
    annots = annots.get_object() if annots is not None else ArrayObject()
    if not isinstance(annots, ArrayObject):
        annots = ArrayObject(annots)
    for a in op["/Annots"]:
        obj = a.get_object()
        if obj.get("/Subtype") != "/Widget":
            continue
        new = obj.clone(writer)
        new_obj = new.get_object()
        new_obj[NameObject("/P")] = page.indirect_reference
        if "/Parent" in new_obj:
            del new_obj["/Parent"]
        ref = writer._add_object(new_obj) if new.indirect_reference is None else new.indirect_reference
        annots.append(ref)
        fields.append(ref)
    page[NameObject("/Annots")] = annots

acro = DictionaryObject()
acro[NameObject("/Fields")] = fields
src_af = ovr.trailer["/Root"]["/AcroForm"]
for k in ("/DA", "/DR"):
    if k in src_af:
        acro[NameObject(k)] = src_af[k].clone(writer)
acro[NameObject("/NeedAppearances")] = __import__("pypdf").generic.BooleanObject(False)
writer._root_object[NameObject("/AcroForm")] = writer._add_object(acro)
writer.add_metadata({"/Title": "GTA VI — Le Guide Ultime (Édition Premium) v1.0",
                     "/Author": "Guide indépendant — non affilié à Rockstar Games",
                     "/Subject": "Guide francophone non officiel de Grand Theft Auto VI",
                     "/Keywords": "GTA 6, GTA VI, guide, Leonida, Vice City, easter eggs, 100%"})
toc = json.load(open(os.path.join(root, "build", "toc.json")))
parent = None
for lvl, label, pg in toc:
    if not pg:
        continue
    if lvl == 1:
        parent = writer.add_outline_item(label, pg - 1)
    else:
        writer.add_outline_item(label, pg - 1, parent=parent)
writer.page_mode = "/UseOutlines"
out = os.path.join(root, "dist", "GTA-VI-Le-Guide-Ultime-Edition-Premium-v1.0.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "wb") as f:
    writer.write(f)
print("ok", out, "fields:", len(fields))
