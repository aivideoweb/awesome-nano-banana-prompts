# Contributing

Thank you for improving the aivideoweb.com Nano Banana 2.1 prompt library.

## Add a meaningful scenario

Edit `data/prompts.json`; use the next available stable ID, a unique descriptive slug and an existing category unless a new category is justified. Provide English and Chinese titles, complete prompts, a recommended aspect ratio, mode, reference requirements and task-specific quality checks. Explain what practical task the recipe solves.

Do not inflate the collection with cosmetic variants. Do not import another gallery's wording, images or contributor records. For any licensed input, document the source and retain required attribution.

## Submit a model output honestly

Default target-model status is `not_tested`. To claim a Nano Banana 2.1 result, include the actual model identifier, provider/client, date, full prompt, output settings, authorized reference inputs and original output. Explain manual edits and selection among retries. Never relabel another model's image as a target-model test.

Add local WebP previews and a generation-manifest entry with a checksum. Avoid external hotlinks. Record observed departures from the prompt; successful appearance does not prove every criterion passed.

## Translate a language

Translate from the same stable IDs. Have a fluent reviewer check phrasing and in-image copy. State whether a contribution is a full catalog or a starter guide. Do not advertise a complete language version before its content exists.

## Build and review

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

Commit the updated data, generated catalogs/pages, local images and manifest together. Inspect the gallery at desktop and mobile widths. Follow `docs/editorial-checklist.md`; use `docs/provenance.md` for source records.

The repository's original text and code use MIT. Generated images are described separately in `assets/README.md`.
