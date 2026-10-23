#!/usr/bin/env python3
"""Run after DNS and HTTPS are ready; inspect diff, commit and push separately."""
from pathlib import Path
from urllib.request import urlopen
import sys

root = Path(__file__).resolve().parents[1]
checks = [
    ('https://www.aluhjewels.com/', 'https://www.aluhjewels.com/', 'const SHOP = "https://shop.aluhjewels.com";'),
    ('https://www.aluhjewels.com/shop.html', 'https://www.aluhjewels.com/shop.html', "var SHOP='https://shop.aluhjewels.com/products/';"),
    ('https://aluhjewels.com/', 'https://www.aluhjewels.com/', 'ALUH Jewels'),
    ('https://wemerson123.github.io/aluh-landing/', 'https://www.aluhjewels.com/', 'ALUH Jewels'),
]
try:
    for url, destination, marker in checks:
        with urlopen(url, timeout=30) as response:
            if response.status != 200 or response.geturl() != destination or marker not in response.read().decode():
                raise RuntimeError('Unexpected destination/content: ' + url)
except Exception as exc:
    sys.exit('SEO remains blocked; no files changed. ' + str(exc))
for name in ('index.html', 'shop.html'):
    path = root / name
    path.write_text(path.read_text().replace('content="noindex, follow"', 'content="index, follow"'))
(root / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://www.aluhjewels.com/sitemap.xml\n')
print('SEO activated locally. Review diff, commit and push to main.')
