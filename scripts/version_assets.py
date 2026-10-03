#!/usr/bin/env python3
"""Refresh local CSS/JS URLs when their contents change, avoiding stale browser caches."""
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
page = ROOT / 'index.html'
html = page.read_text()
for name in ('style.css', 'script.js'):
    digest = sha256((ROOT / name).read_bytes()).hexdigest()[:12]
    pattern = rf'((?:href|src)="){re.escape(name)}(?:\?[^"\s]*)?(")'
    html, count = re.subn(pattern, lambda match: f'{match[1]}{name}?v={digest}{match[2]}', html)
    if count != 1:
        raise SystemExit(f'Expected one reference to {name}, found {count}')
    print(f'{name}?v={digest}')
if html != page.read_text():
    page.write_text(html)
