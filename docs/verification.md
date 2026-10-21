# Verification record — 2026-10-21

## Content and build

`python3 scripts/build.py` completed successfully. `python3 scripts/validate.py` passed for 48 unique bilingual records, 12 categories, 12 image-manifest records and 49 static HTML pages. Local Markdown and HTML links resolve; preview checksums match their files; all target-model entries retain their untested status.

## Visual review

All 12 new images were reviewed together at contact-sheet scale. Observed deviations are recorded per image in `assets/generation-manifest.json`. This review is sufficient for an illustrative library preview, not print approval, detailed typography certification or a model benchmark.

A desktop browser review found and corrected image stretching caused by fixed HTML dimensions. The delivery stylesheet now keeps the cover's natural aspect ratio and uses cropped preview cards.

## Browser behavior

Verified in the local in-app browser:

- The homepage renders its heading, cover and disclosure.
- Searching for `海报` returns 3 matching entries.
- Searching for a nonexistent term displays 0 entries and a clear empty state.
- Selecting the storyboard category displays its 4 entries.
- Opening the fox courier entry shows its image, bilingual prompts and quality checks.
- The English copy button displays `Copied / 已复制`.

No separate mobile-device, screen-reader or production-host test was performed. Responsive styling and semantic labels are provided, but are not a substitute for those checks.

## Limits

No Gemini or flaq credentials were configured in the environment. No Nano Banana 2.1 request was made. The repository has not been deployed, pushed or benchmarked; no live search indexing or ranking result is claimed.
