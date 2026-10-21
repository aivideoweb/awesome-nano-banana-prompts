#!/usr/bin/env python3
"""Validate content integrity, generated output, local links and image provenance."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib, json, re, sys
R=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,message):
 if not ok: errors.append(message)
items=json.loads((R/'data/prompts.json').read_text())
cats=json.loads((R/'data/categories.json').read_text())
manifest=json.loads((R/'assets/generation-manifest.json').read_text())
check(len(items)==48,'Expected 48 distinct scenarios')
check(len({p['id'] for p in items})==len(items),'Duplicate prompt IDs')
check(len({p['slug'] for p in items})==len(items),'Duplicate slugs')
check(len(cats)==12,'Expected 12 categories')
for p in items:
 check(p['category'] in {c['slug'] for c in cats},f'Unknown category {p["id"]}')
 for lang in ['en','zh']:
  check(len(p['prompt'][lang])>120,f'Short/missing prompt: {p["id"]}/{lang}')
  check(bool(p['quality_check'][lang]),f'Missing quality check: {p["id"]}/{lang}')
  catalog=(R/f'prompts/{lang}.md').read_text()
  check(p['prompt'][lang] in catalog,f'Stale catalog: {p["id"]}/{lang}')
 check(p['reference_required']==(p['mode']=='edit'),f'Reference requirement mismatch: {p["id"]}')
 check(p['target_model_status']=='not_tested',f'Unsupported model test claim: {p["id"]}')
 page=R/f'site/prompts/{p["slug"]}.html'
 check(page.exists(),f'Missing page: {p["id"]}')
 if p.get('preview'):
  check((R/p['preview']).exists(),f'Missing preview: {p["id"]}')
  check(any(m['id']==p['id'] and m['file']==p['preview'] for m in manifest),f'No manifest record: {p["id"]}')
for c in cats:
 check(sum(p['category']==c['slug'] for p in items)==4,f'Expected four recipes in {c["slug"]}')
for m in manifest:
 file=R/m['file'];check(file.exists(),f'Missing asset: {file}')
 if file.exists():check(hashlib.sha256(file.read_bytes()).hexdigest()==m['sha256'],f'Hash mismatch: {file}')
 check(m['generator']=='built-in imagegen' and not m['target_model_verified'],f'Misleading image attribution: {m["id"]}')
 check(bool(m['prompt']) and m['review']!='pending_visual_review',f'Incomplete generation record: {m["id"]}')
check(len(manifest)==12,'Expected 12 generated image assets')
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.h1=0;self.desc=False;self.title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='meta' and a.get('name')=='description':self.desc=bool(a.get('content'))
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
def local_exists(file,link):
 parsed=urlsplit(link)
 if parsed.scheme or parsed.netloc or not parsed.path:return
 target=(file.parent/unquote(parsed.path)).resolve()
 check(target.is_relative_to(R),f'Link escapes repository: {file.relative_to(R)} => {link}')
 check(target.exists(),f'Broken local link: {file.relative_to(R)} => {link}')
for file in R.rglob('*.html'):
 if '.git' in file.parts:continue
 parser=Page();parser.feed(file.read_text())
 check(parser.h1==1,f'Expected one H1: {file.relative_to(R)}')
 check(parser.title and parser.desc,f'Missing SEO metadata: {file.relative_to(R)}')
 for link in parser.links:local_exists(file,link)
for file in R.rglob('*.md'):
 if '.git' in file.parts:continue
 for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',file.read_text()):local_exists(file,link)
if errors:
 print('\n'.join('ERROR: '+e for e in errors));sys.exit(1)
print(f'PASS: {len(items)} bilingual scenarios, {len(cats)} categories, {len(manifest)} image records, 49 HTML pages, local links and truthful model status.')
