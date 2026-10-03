#!/usr/bin/env python3
"""Dependency-free checks for static portfolio links, assets, and metadata."""
from html.parser import HTMLParser
from hashlib import sha256
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.assets, self.errors = set(), [], [], []
        self.h1_count = 0
        self.metadata = set()

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if 'id' in data:
            if data['id'] in self.ids:
                self.errors.append(f"Duplicate id: {data['id']}")
            self.ids.add(data['id'])
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'meta':
            self.metadata.add(data.get('name') or data.get('property'))
        if tag == 'a':
            self.links.append(data.get('href', ''))
            if data.get('target') == '_blank' and not {'noopener', 'noreferrer'}.issubset(data.get('rel', '').split()):
                self.errors.append(f"New-tab link missing safe rel: {data.get('href')}")
        if tag in ('script', 'img') and 'src' in data:
            self.assets.append(data['src'])
        if tag == 'link' and data.get('rel') != 'canonical':
            self.assets.append(data.get('href', ''))
        if tag == 'img' and not all(k in data for k in ('alt', 'width', 'height')):
            self.errors.append(f"Image missing alt or intrinsic size: {data.get('src')}")

site = SiteParser()
site.feed((ROOT / 'index.html').read_text())
for link in site.links + site.assets:
    url = urlsplit(link)
    if not link:
        site.errors.append('Empty link or asset URL')
    elif not url.scheme and not url.netloc:
        if url.path and not (ROOT / unquote(url.path)).is_file():
            site.errors.append(f'Missing local file: {url.path}')
        elif url.path in ('style.css', 'script.js'):
            digest = sha256((ROOT / url.path).read_bytes()).hexdigest()[:12]
            if parse_qs(url.query).get('v') != [digest]:
                site.errors.append(f'Stale asset version for {url.path}: run python3 scripts/version_assets.py')
        if url.fragment and not url.path and unquote(url.fragment) not in site.ids:
            site.errors.append(f'Missing section target: {url.fragment}')
required = {'description', 'viewport', 'og:title', 'og:description', 'og:url', 'og:image', 'twitter:card'}
if missing := required - site.metadata:
    site.errors.append(f'Missing metadata: {sorted(missing)}')
if site.h1_count != 1:
    site.errors.append(f'Expected one h1, found {site.h1_count}')
if not (ROOT / 'files/Andrew_Chen_Resume.pdf').read_bytes().startswith(b'%PDF-'):
    site.errors.append('Resume is not a PDF')
if not (ROOT / '.nojekyll').is_file():
    site.errors.append('Missing .nojekyll')
ET.parse(ROOT / 'sitemap.xml')
if site.errors:
    raise SystemExit('\n'.join(site.errors))
print(f'PASS: {len(site.links)} links, {len(site.assets)} assets, unique anchors, metadata, PDF, sitemap, and Pages marker.')
print('External URL availability and browser behavior require separate checks.')
