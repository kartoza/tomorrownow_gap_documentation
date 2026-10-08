"""Check the guide against an API checkout and its rendered HTML.

Usage: python scripts/check_api_guide.py /path/to/tomorrownow_gap
Build docs/site first with the repository's MkDocs configuration.
"""

import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / 'docs/src/developer/api/guide'
SITE = ROOT / 'docs/site'
FIXTURES = Path(sys.argv[1]) / 'django_project/gap/fixtures'
RETIRED = {
    'google_gencast',
    'cbam_shortterm_forecast', 'cbam_shortterm_hourly_forecast',
    'nigeria_daily_forecast', 'nigeria_hourly_forecast',
}
# Still served for existing integrations; listed under legacy products.
NOT_LISTED = set()


def fixture(name):
    return {r['pk']: r['fields'] for r in json.loads((FIXTURES / name).read_text())}


def check(condition, message):
    if not condition:
        raise AssertionError(message)


types = fixture('4.dataset_type.json')
datasets = fixture('5.dataset.json')
attributes = fixture('7.attribute.json')
mappings = fixture('8.dataset_attribute.json')
expected = {}
for pk, dataset in datasets.items():
    product = types[dataset['type']]['variable_name']
    if (product in RETIRED or product in NOT_LISTED or not dataset.get('is_active', True)
            or dataset.get('is_internal_use', False)):
        continue
    names = expected.setdefault(product, set())
    for mapping in mappings.values():
        attribute = attributes[mapping['attribute']]
        if (mapping['dataset'] == pk and mapping.get('is_active', True)
                and attribute.get('is_active', True)):
            names.add(attribute['variable_name'])
manifest = json.loads((ROOT / 'docs/reviews/2026-09-28-api-catalogue.json').read_text())['products']
check(set(manifest) == set(expected), 'Product list differs from API fixtures')
for product, fields in expected.items():
    record = manifest[product]
    check(set(record['attributes']) == fields, f'Manifest fields: {product}')
    page = GUIDE / 'measurements/attributes-reference' / record['page']
    section = page.read_text().split(f'## `{product}`\n', 1)[1].split('\n## ', 1)[0]
    actual = set(re.findall(r'^\| `([^`]+)` \|', section, re.M))
    check(actual == fields, f'Rendered-source field table: {product}')
    html_path = SITE / 'developer/api/guide/measurements/attributes-reference' / page.stem / 'index.html'
    soup = BeautifulSoup(html_path.read_text(), 'html.parser')
    check(all(soup.select_one('article').find(string=f) for f in fields), f'HTML fields: {product}')

checked = 0
for page in (SITE / 'developer/api/guide').rglob('*.html'):
    soup = BeautifulSoup(page.read_text(), 'html.parser')
    article = soup.select_one('article')
    if article is None:  # redirect page
        continue
    for link in article.select('[href]'):
        url = urlparse(link['href'])
        if url.scheme or url.netloc or not url.path:
            continue
        target = (SITE / unquote(url.path.lstrip('/')) if url.path.startswith('/')
                  else page.parent / unquote(url.path)).resolve()
        if target.is_dir():
            target /= 'index.html'
        check(target.exists(), f'Broken link: {page} -> {link["href"]}')
        if url.fragment and target.suffix == '.html':
            dest = BeautifulSoup(target.read_text(), 'html.parser')
            check(dest.find(id=unquote(url.fragment)), f'Broken anchor: {link["href"]}')
        checked += 1

for page in GUIDE.rglob('*.md'):
    for language, code in re.findall(r'```(\w+)\n(.*?)```', page.read_text(), re.S):
        if language == 'python':
            ast.parse(code)
for page in (ROOT / 'examples').glob('*.py'):
    ast.parse(page.read_text())
notebook = json.loads((ROOT / 'examples/sample.ipynb').read_text())
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        ast.parse(''.join(cell['source']))
        check(not cell['outputs'], 'Notebook has saved outputs')
collection = json.loads((GUIDE / 'assets/tngap_api.postman_collection.json').read_text())
for item in collection['item']:
    params = {q['key']: q['value'] for q in item['request']['url'].get('query', [])}
    if 'product' in params:
        check(params['product'] in expected, 'Postman product')
        check(set(params['attributes'].split(',')) <= expected[params['product']], 'Postman fields')
print(f'PASS: {len(expected)} products, {sum(map(len, expected.values()))} fields, '
      f'{checked} local links, Python snippets, notebook and Postman queries')
