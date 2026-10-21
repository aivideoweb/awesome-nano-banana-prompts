# Editorial checklist / 内容发布检查

## A prompt must solve a concrete task

- Identify the user, asset and intended use before choosing a visual style.
- Use a distinct brief rather than changing only palette, product color or language.
- Specify subject, composition, exact copy, exclusions and one meaningful review criterion.
- Identify reference-image roles and elements that must remain unchanged.
- State when the result is only a concept, such as UI mockups, game terrain or architectural studies.

## Facts and evidence

- Verify model names and dated feature claims against official documentation.
- Do not invent benchmark scores, successful tests, client results, usage statistics or rankings.
- Keep target-model tests separate from previews created elsewhere.
- Do not label a single cherry-picked generation as a repeatable success rate.

## Search usefulness

- Give every page one descriptive H1 and a summary matching the task.
- Use clear category navigation, stable slugs and meaningful link labels.
- Keep important prompt text in static HTML; search should enhance navigation rather than hide content from readers without JavaScript.
- Write image alt text describing the picture and its purpose, without keyword repetition.
- Publish only languages actually provided. Do not create empty language landing pages.
- Add FAQ answers that address real use questions; do not fabricate review or rating markup.
- Avoid inflated claims such as “perfect text,” “guaranteed commercial rights” or “best model.”

## Human editorial pass

Read the page aloud. Remove repeated slogans, vague praise and unsupported experience claims. Keep concrete examples and failure checks. If a sentence could describe almost any AI tool, replace it with useful guidance or remove it.

## Release gate

Run `python3 scripts/build.py` and `python3 scripts/validate.py`. Inspect preview images and open the gallery in a browser. Review mobile layout, search, category filtering and copying. Check model status labels, language scope and the image manifest before publication.
