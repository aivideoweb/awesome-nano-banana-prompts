# Publishing and SEO handoff

The repository contains a static, portable gallery, not a deployed website. No live gallery URL or search performance is claimed.

## Local preview

From the repository root:

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 -m http.server 8000
```

Open `http://localhost:8000/site/`. Keep the repository layout intact: HTML uses shared files in `assets/`, `docs/`, `prompts/` and `data/`.

## Hosting layout

For static hosting, publish the repository's public files with `site/` as a subdirectory, preserving the relative paths. Do not configure `site/` alone as the publish root without also moving assets and rebuilding links. Avoid publishing `.git/` and any local-only configuration.

If you prefer a gallery at the domain root, adapt the build script's path handling and validate after the change. GitHub renders Markdown documentation directly; it does not execute repository HTML as a website.

## Included search foundations

- An English homepage with a descriptive title and meta description.
- Seventy-two static detail pages with unique titles, summaries, bilingual prompt bodies and contextual review instructions.
- Category navigation, plain links, readable URLs and descriptive image alt text.
- `CreativeWork` structured data describing authored recipes; no invented reviews, ratings or verified-model claims.
- Local WebP assets and lazy-loaded preview cards.

## Configure after choosing a public URL

Set canonical URLs and absolute Open Graph image URLs using the actual deployed host. Generate a sitemap containing only public 200-status pages; reference it from that host's robots file. Do not invent a canonical domain or use a production URL before it exists.

If you later publish fully localized HTML, give each language its own URL, translated metadata and reciprocal hreflang links. The current Japanese and Spanish README introductions do not imply a fully translated gallery.

## Content update policy

There is no scheduled sync or automatic third-party scraping. Updates are reviewed changes to the data and its generated pages. A useful release adds a distinct scenario, a reviewed translation, a documented failure or a transparent real-model test. Keep counts and the changelog consistent.

For measurement after deployment, use actual indexing, query and click data. Search ranking cannot be promised from metadata or keyword density alone.

Public X sources have their own crawlable `site/sources.html` page and per-recipe citations. Keep this page linked when deploying; do not strip source attribution during localization.
