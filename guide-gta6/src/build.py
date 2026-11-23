# -*- coding: utf-8 -*-
"""Assemble le guide en HTML (pages A5 fixes) : python3 src/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book import Book
import content_a as A, content_b as B, content_c as C, content_d as D

book = Book()
A.cover(book)
slots = [book.placeholder("toc1"), book.placeholder("toc2")]
A.disclaimer(book)
A.how_to(book)
A.part1(book); A.part2(book)
B.part3(book); B.part4(book); B.part5(book)
C.part6(book); C.part7(book); C.part8(book)
D.part9(book); D.part10(book)
D.latest(book)
D.index_pages(book)
D.sources_pages(book)
D.back_cover(book)
D.toc(book, slots)
book.anchor_page["sommaire"] = slots[0] + 1
out = os.path.join(os.path.dirname(__file__), "..", "build", "guide.html")
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w", encoding="utf-8").write(book.html())
import json
json.dump([[lvl, label, book.anchor_page.get(aid)] for lvl, label, aid in
           [(1, "Sommaire", "sommaire")] + book.toc], open(os.path.join(os.path.dirname(out), "toc.json"), "w"), ensure_ascii=False)
print("pages:", len(book.pages), "toc:", len(book.toc), "index:", len(book.index))
