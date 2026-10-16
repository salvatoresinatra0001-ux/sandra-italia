#!/usr/bin/env python3
"""Verify Sandra Italia static pages before GitHub Pages deploy."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FAILURES = []

class SitePage(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.h1 = 0
        self.title = False
        self.description = False
        self.main = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.title = True
        if tag == "main" and attrs.get("id") == "main":
            self.main = True
        if tag == "meta" and attrs.get("name") == "description":
            self.description = bool(attrs.get("content"))
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

def local_target(page, url):
    if not url or url.startswith(("#", "//")):
        return None
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        return None
    local = unquote(parsed.path)
    if not local:
        return None
    if local.startswith("/"):
        return ROOT / local.lstrip("/")
    target = (page.parent / local).resolve()
    if not target.is_relative_to(ROOT):
        FAILURES.append(f"{page.relative_to(ROOT)}: link outside repository {url}")
        return None
    if target.is_dir() or local.endswith("/"):
        target = target / "index.html"
    return target

pages = list(ROOT.rglob("*.html"))
if not pages:
    FAILURES.append("No HTML pages found")
for page in pages:
    doc = SitePage(page)
    doc.feed(page.read_text(encoding="utf-8"))
    name = str(page.relative_to(ROOT))
    if doc.h1 != 1:
        FAILURES.append(f"{name}: expected one <h1>, found {doc.h1}")
    if not doc.title or not doc.description:
        FAILURES.append(f"{name}: missing page title or meta description")
    if name != "gallerie/copertine-medium/index.html" and not doc.main:
        FAILURES.append(f"{name}: missing <main id='main'>")
    for link in doc.links:
        target = local_target(page, link)
        if target is not None and not target.is_file():
            FAILURES.append(f"{name}: missing local asset {link}")

for required in ("index.html", "fotografie.html", "edizioni.html", "assets/css/style.css", "assets/js/site.js", "assets/img/favicon.svg"):
    if not (ROOT / required).is_file():
        FAILURES.append(f"Required file missing: {required}")
try:
    ET.parse(ROOT / "sitemap.xml")
except (OSError, ET.ParseError) as exc:
    FAILURES.append(f"Invalid sitemap: {exc}")

if FAILURES:
    for error in FAILURES:
        print("FAIL:", error, file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: {len(pages)} HTML pages, internal assets, structure and sitemap")
