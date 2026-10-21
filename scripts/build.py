#!/usr/bin/env python3
"""Build Markdown catalogs and a portable, dependency-free static gallery."""
from pathlib import Path
import json, html, re
R=Path(__file__).resolve().parents[1]
items=json.loads((R/'data/prompts.json').read_text())
cats=json.loads((R/'data/categories.json').read_text())
H=html.escape
sources=json.loads((R/'data/sources.json').read_text())
source_index={x['id']:x for x in sources}
count=len(items)
x_count=sum(p.get('origin')=='x_inspired_adaptation' for p in items)
def source_markdown(p,lang):
 if not p.get('sources'): return []
 result=['**'+('X 案例来源（社区报告，未独立复现）' if lang=='zh' else 'X source (community report; not independently reproduced)')+'**','']
 for ref in p['sources']:
  src=source_index[ref['source_id']]
  result += [f"- [{src['author']} · {src['title']}]({src['url']}) · {src['published_date']} · {ref['section']}"]
 result += ['',p['adaptation'][lang],'']
 return result
def source_html(p):
 if not p.get('sources'): return ''
 refs=[]
 for ref in p['sources']:
  src=source_index[ref['source_id']]
  refs.append(f'<li><a href="{H(src["url"],quote=True)}">{H(src["author"])} — {H(src["title"])}</a> · {src["published_date"]}<br>{H(ref["section"])}</li>')
 return '<section><h2>X case source / 案例来源</h2><ul>'+''.join(refs)+'</ul><p>'+H(p['adaptation']['en'])+'</p><p lang="zh-CN">'+H(p['adaptation']['zh'])+'</p><p>Source authors identify Nano Banana 2.1. Their reports are not independent tests by this project. A tutorial proposal is not a demonstrated result.</p><p><a href="../sources.html">Review all sources and evidence levels</a></p></section>'

for lang in ['zh','en']:
 out=['# Nano Banana 2.1 '+('提示词完整目录' if lang=='zh' else 'Prompt Catalog'),'', '[aivideoweb.com](https://aivideoweb.com) · [Home](../README.md) · [JSON](../data/prompts.json)','',(f'{count} 条制作方案，其中 {x_count} 条根据公开 X 案例主题改编。中英文为同一条目的两种语言版本，不重复计数。所有改编均未独立复现。' if lang=='zh' else f'{count} recipes, including {x_count} adaptations inspired by public X case themes. Translations are not additional entries. Adaptations have not been independently reproduced.'),'']
 for c in cats:
  out += [f'## {c[lang]}','']
  for p in [p for p in items if p['category']==c['slug']]:
   out += [f"### {p['id']} · {p['title'][lang]}",'',f"`{p['mode']}` · `{p['aspect_ratio']}` · "+('需上传自有/获授权参考图' if p['reference_required'] else '无需参考图') if lang=='zh' else f"`{p['mode']}` · `{p['aspect_ratio']}` · "+('Authorized reference images required' if p['reference_required'] else 'No reference required'),'']
   if p.get('preview'):
    out += [f"![{p['title'][lang]} — original illustrative preview](../{p['preview']})",'',('新生成的说明性展示图；由内置 imagegen 工具生成，非 Nano Banana 2.1 实测。' if lang=='zh' else 'New illustrative preview generated with the built-in imagegen tool; not a Nano Banana 2.1 test.'),'']
   out += source_markdown(p,lang)
   out += ['```text',p['prompt'][lang],'```','',('**验收：** ' if lang=='zh' else '**Review:** ')+p['quality_check'][lang],'',('**单点修正：** 仅修正上述验收中不合格的部分，保持主体、构图、色调和其他文字不变。' if lang=='zh' else '**Focused revision:** Fix only the failed review criterion above. Preserve the subject, composition, palette and all other lettering.'),'',('**模型建议：** 先选 1K 验证构图，再按用途选 2K/4K；画幅和分辨率在客户端设置，不依赖提示词文字。编辑类先上传参考图。' if lang=='zh' else '**Model workflow:** Draft at 1K, then select 2K/4K if needed. Set aspect ratio and resolution in your client; mentioning them in a prompt does not configure the API. Upload references first for edits.'),'']
 (R/f'prompts/{lang}.md').write_text('\n'.join(out)+'\n')
site=R/'site'; (site/'prompts').mkdir(parents=True,exist_ok=True)
css='''*{box-sizing:border-box}body{margin:0;background:#faf8f2;color:#192c32;font:16px/1.65 system-ui,sans-serif}a{color:#09685d}header,main,footer{max-width:1200px;margin:auto;padding:28px}h1{font-size:clamp(32px,5vw,64px);line-height:1.1;max-width:900px}h2{line-height:1.25}.eyebrow{font-size:13px;letter-spacing:.15em;text-transform:uppercase;color:#176b62}.lead{max-width:800px;font-size:19px}.hero{width:100%;height:auto;border-radius:20px;display:block}nav{display:flex;gap:18px;flex-wrap:wrap}.controls{display:flex;gap:12px;flex-wrap:wrap;margin:32px 0}input,select,button{font:inherit;padding:12px;border:1px solid #a6b9b3;background:white;border-radius:8px}input{flex:1;min-width:220px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}.card{background:white;border:1px solid #d5ded7;border-radius:16px;overflow:hidden}.card img{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;display:block}.card .body{padding:20px}.card h2{font-size:22px;margin:8px 0}.badge{font-size:12px;color:#46595a}.no-preview{padding:40px 20px;background:#e9eee6;font-size:20px;min-height:150px;display:flex;align-items:center}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#edf0e9;padding:24px;border-radius:12px}article{max-width:850px}article img{max-width:100%;height:auto;border-radius:16px}.note{border-left:4px solid #e5ad2f;padding:10px 18px;background:#fff6dc}.hidden,[hidden]{display:none!important}button{cursor:pointer;background:#09685d;color:white}a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #e5ad2f;outline-offset:4px}footer{border-top:1px solid #d5ded7;font-size:14px}'''
(site/'style.css').write_text(css)
def shell(title,desc,body,depth=0,lang='en',schema=None):
 prefix='../'*depth
 structured='' if not schema else '<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script>'
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{H(title)}</title><meta name="description" content="{H(desc)}"><meta property="og:title" content="{H(title)}"><meta property="og:description" content="{H(desc)}"><meta property="og:type" content="website"><meta name="color-scheme" content="light"><link rel="stylesheet" href="{prefix}style.css">{structured}</head><body><header><nav><a href="{prefix}index.html">Prompt Library</a><a href="{prefix}sources.html">X case sources</a><a href="https://aivideoweb.com">aivideoweb.com</a><a href="https://github.com/aivideoweb/awesome-nano-banana-prompts">GitHub</a></nav></header>{body}<footer>Created by the aivideoweb.com team · Independent open-source project · Illustrative previews use built-in imagegen, not Nano Banana 2.1. Model tests are pending.</footer></body></html>'''
cards=[]
for p in items:
 slug=p['slug']; title=p['title']['en']; zh=p['title']['zh']
 # Asset paths resolve from repo/site; no remote image dependency.
 img=f'<img src="../{p["preview"]}" alt="{H(title)} — original illustrative preview" loading="lazy" width="800" height="600">' if p.get('preview') else '<div class="no-preview">Prompt recipe · 提示词方案</div>'
 searchable=' '.join([title,zh,p['category'],p['prompt']['en'],p['prompt']['zh']]+[source_index[ref['source_id']]['handle'] for ref in p.get('sources',[])])
 origin='x_inspired_adaptation' if p.get('sources') else 'original'
 origin_label='X case adaptation / X案例改编' if p.get('sources') else 'Original recipe / 原创方案'
 cards.append(f'<article class="card" data-category="{p["category"]}" data-origin="{origin}" data-search="{H(searchable,quote=True)}">{img}<div class="body"><span class="badge">{p["id"]} · {p["aspect_ratio"]} · {p["mode"]}</span><h2><a href="prompts/{slug}.html">{H(title)}</a></h2><p lang="zh-CN">{H(zh)}</p><p>{"Reference required" if p["reference_required"] else "Text-to-image"} · Target-model test pending</p><p class="badge">{origin_label}</p></div></article>')
 image=f'<img src="../../{p["preview"]}" alt="{H(title)} — illustrative preview">' if p.get('preview') else ''
 body=f'<main><article><p class="eyebrow">{p["id"]} / {p["category"]}</p><h1>{H(title)}</h1><p class="lead" lang="zh-CN">{H(zh)}</p><p>Suggested frame: {p["aspect_ratio"]} · Mode: {p["mode"]} · Target: Nano Banana 2.1</p>{image}<p class="note">Target-model test pending. Any preview on this page is an original imagegen illustration, not evidence of Nano Banana output. {"Upload authorized references before running this edit." if p["reference_required"] else "No reference image required."}</p>{source_html(p)}<h2>English prompt</h2><pre id="en">{H(p["prompt"]["en"])}</pre><button data-copy="en">Copy English prompt</button><h2 lang="zh-CN">中文提示词</h2><pre id="zh" lang="zh-CN">{H(p["prompt"]["zh"])}</pre><button data-copy="zh">复制中文提示词</button><p role="status" id="copy-status" aria-live="polite"></p><h2>Quality review</h2><p>{H(p["quality_check"]["en"])}</p><p lang="zh-CN">{H(p["quality_check"]["zh"])}</p><h2>How to iterate</h2><p>Set aspect ratio and resolution in your image client. Start at 1K. Fix one failed criterion at a time while preserving everything else; restart from your original reference if identity drifts.</p><p><a href="../index.html">Browse all {count} prompts</a> · <a href="../../docs/model-guide.md">Model guide</a></p></article></main><script src="../copy.js"></script>'
 schema={'@context':'https://schema.org','@type':'CreativeWork','name':title,'description':p['prompt']['en'],'inLanguage':['en','zh-CN'],'creator':{'@type':'Organization','name':'aivideoweb.com','url':'https://aivideoweb.com'},'license':'https://opensource.org/license/mit'}
 (site/f'prompts/{slug}.html').write_text(shell(f'{title} | Nano Banana 2.1 Prompt',f'{title}: an original bilingual Nano Banana 2.1 prompt with composition, lettering constraints and review criteria. Created by aivideoweb.com.',body,1,schema=schema))
opts=''.join(f'<option value="{c["slug"]}">{H(c["en"])} / {H(c["zh"])} ({sum(p["category"]==c["slug"] for p in items)})</option>' for c in cats)
body=f'''<main><p class="eyebrow">aivideoweb.com / open creative recipes</p><h1>Nano Banana 2.1 prompts for everyday creative work</h1><p class="lead">{count} practical recipes, including {x_count} X case adaptations. {len(cats)} categories. English and Chinese prompts with exact text instructions, composition constraints and review criteria.</p><img class="hero" src="../assets/images/cover.webp" alt="Original aivideoweb.com creative prompt library cover: product photography, botanical diagram and fox courier illustration" width="1672" height="941"><p class="note">These prompts target Nano Banana 2.1. Preview images were created with built-in imagegen and are illustrative. No Nano Banana benchmark or verified output is claimed. <a href="sources.html">Browse {len(sources)} public X source records</a>; source reports and our rewritten recipes are labeled separately.</p><section aria-label="Search prompts"><div class="controls"><input type="search" id="search" aria-label="Search English or Chinese prompts" placeholder="Search product, storyboard, 海报…"><select id="category" aria-label="Category"><option value="">All categories / 全部分类</option>{opts}</select><select id="origin" aria-label="Recipe origin"><option value="">All recipes / 全部方案</option><option value="x_inspired_adaptation">X case adaptations / X案例改编</option><option value="original">Original collection / 初始方案</option></select></div><p id="count" aria-live="polite">{count} prompts</p><p id="empty" hidden>No matching prompts. Try a broader search.</p><div class="grid">{''.join(cards)}</div></section><section><h2>How do I use a Nano Banana 2.1 prompt?</h2><p>Open an entry, copy your preferred language, replace the fictional subject with your own brief and select the aspect ratio in your image tool. Editing recipes require authorized reference images. Generate a small draft, check the listed criteria, then revise one issue at a time.</p><h2>Can I use the library commercially?</h2><p>The repository's original text and code use the MIT license. Generated images are not a guarantee of exclusive rights or clearance. Review any visible marks, people and third-party materials before publication.</p><h2>Are these verified model outputs?</h2><p>No. The target model is documented separately from the illustrative preview generator. Each entry records its status in the JSON catalog.</p><h2>Explore the source</h2><p><a href="../prompts/en.md">English catalog</a> · <a href="../prompts/zh.md">中文目录</a> · <a href="../docs/model-guide.md">Model guide</a> · <a href="../data/prompts.json">JSON data</a></p></section></main><script src="gallery.js"></script>'''
(site/'index.html').write_text(shell(f'Nano Banana 2.1 Prompts: {count} Image Recipes | aivideoweb.com',f'Explore {count} Nano Banana 2.1 prompts for products, ads, portraits, storyboards and image editing. Bilingual recipes with quality checks by aivideoweb.com.',body))
(site/'gallery.js').write_text('''const search = document.querySelector('#search');
const category = document.querySelector('#category');
const origin = document.querySelector('#origin');
const cards = [...document.querySelectorAll('.card')];
function filter() {
  const query = search.value.trim().toLocaleLowerCase();
  let visible = 0;
  for (const card of cards) {
    const match = (!category.value || card.dataset.category === category.value) && (!origin.value || card.dataset.origin === origin.value) && card.dataset.search.toLocaleLowerCase().includes(query);
    card.hidden = !match;
    if (match) visible++;
  }
  document.querySelector('#count').textContent = `${visible} / ${cards.length} prompts`;
  document.querySelector('#empty').hidden = visible !== 0;
}
search.addEventListener('input', filter);
category.addEventListener('change', filter);
origin.addEventListener('change', filter);
''')
(site/'copy.js').write_text('''document.querySelectorAll('[data-copy]').forEach(button => {
  button.addEventListener('click', async () => {
    const status = document.querySelector('#copy-status');
    try {
      await navigator.clipboard.writeText(document.getElementById(button.dataset.copy).textContent);
      status.textContent = 'Copied / 已复制';
    } catch {
      status.textContent = 'Select the prompt text and copy manually / 请选中文字手动复制';
    }
  });
});
''')
print(f'Built two complete catalogs, a searchable gallery and {len(items)} crawlable detail pages.')

# Render the same evidence registry into readable Markdown and a crawlable source page.
md=['# X 案例来源与改编记录 / X Case Sources','',f'{len(sources)} 个公开来源记录 · {x_count} 条改编方案 · 浏览器核查日期：2026-10-21','',
'来源提到的2.1型号为发布者自述；本项目未调用其生成端点独立复现。改编提示词是新写的制作方案，不冒充原帖逐字提示词。未下载或重发来源图片。','',
'## 阅读方法','',
'长文中可见完整提示词的章节标为可用；仅展示图片的帖子明确标注原提示词不可得。教程建议与展示结果分开；转引帖只作线索，不再次计数。','']
blocks=[]
for src in sources:
 linked=[p for p in items if any(ref['source_id']==src['id'] for ref in p.get('sources',[]))]
 md += [f"## {src['id']} · {src['author']}",'',f"[{src['title']}]({src['url']})",'',f"Published: {src['published_date']} · Accessed: {src['accessed_on']} · Evidence: `{src['evidence_level']}`",'',src['summary']['zh'],'',src['summary']['en'],'',f"Original prompt available in inspected source: {src['source_prompt_available']}. Independently reproduced: false.",'']
 links=[]
 for recipe in linked:
  md += [f"- [{recipe['id']} · {recipe['title']['zh']}](../site/prompts/{recipe['slug']}.html)"]
  links.append(f'<li><a href="prompts/{recipe["slug"]}.html">{recipe["id"]} · {H(recipe["title"]["en"])} / {H(recipe["title"]["zh"])}</a></li>')
 md += ['']
 blocks.append(f'<section id="{src["id"]}"><h2>{src["id"]} · {H(src["author"])}</h2><p><a href="{H(src["url"],quote=True)}">{H(src["title"])}</a></p><p>{src["published_date"]} · {H(src["evidence_level"])}</p><p>{H(src["summary"]["en"])}</p><p lang="zh-CN">{H(src["summary"]["zh"])}</p><p>Source prompt available: {src["source_prompt_available"]}. Independently reproduced: false. Source media not imported.</p><ul>{"".join(links)}</ul></section>')
(R/'docs/x-case-sources.md').write_text('\n'.join(md)+'\n')
(site/'sources.html').write_text(shell('Nano Banana 2.1 X Case Sources | aivideoweb.com','Public X source records, evidence levels and links to adapted bilingual image prompts.',f'<main><article><p class="eyebrow">aivideoweb.com / evidence register</p><h1>X case sources / X案例来源</h1><p class="lead">{len(sources)} public source records · {x_count} rewritten recipes · Reviewed 2026-10-21</p><p class="note">Public model claims belong to their publishers. Our adaptations are not the original prompts and have not been independently reproduced. Original source images remain at their source.</p>{"".join(blocks)}</article></main>'))
