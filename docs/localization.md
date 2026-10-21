# Multilingual image prompts / 多语言本地化

A localized image needs more than translated words. Keep the scene specification separate from the exact copy; then check glyphs, line length, reading direction and layout in the resulting image.

## What is actually translated here?

| Resource | English | 简体中文 | 日本語 | Español |
|---|---|---|---|---|
| Project introduction | Complete | Complete | Localized starter | Localized starter |
| 48-scenario catalog | Complete | Complete | Not yet | Not yet |
| Search terms in gallery | Yes | Yes | No | No |

Do not count language variants as additional original scenarios. The prompts can request text in other languages, but language support does not guarantee correct output.

## A safer localization workflow

1. Finalize a short source headline and button, with no unverified claims.
2. Write or commission a natural target-language version. Translate intent rather than preserving awkward word order.
3. Include the exact target copy in quotation marks; identify which text box it replaces.
4. Keep the subject, identity, layout, prices and dates unchanged unless the brief asks for changes.
5. Review the actual generated pixels with a speaker of the language. Correct missing accents, punctuation, fallback glyphs or unwanted translations.

## Exact-copy examples

These are original sample campaign lines. They are short starting points, not full catalog translations.

| Language | Headline | Secondary line |
|---|---|---|
| English | Create together | Make room for ideas |
| 简体中文 | 一起创作 | 给灵感留点空间 |
| 繁體中文 | 一起創作 | 為靈感留點空間 |
| 日本語 | 一緒につくろう | アイデアが育つ場所 |
| 한국어 | 함께 만들어요 | 아이디어를 위한 공간 |
| Español | Crea en equipo | Espacio para tus ideas |
| Français | Créons ensemble | Place aux idées |
| Deutsch | Gemeinsam gestalten | Raum für Ideen |
| Português | Vamos criar juntos | Espaço para ideias |
| العربية | لنبدع معًا | مساحة للأفكار |

For Arabic, explicitly request right-to-left composition and preserve connected glyphs. Have a native speaker check shaping and punctuation before publishing. For Chinese and Japanese, prefer deliberate line breaks; avoid forcing long phrases into narrow Latin-style buttons.

## Example: localize an owned event poster

```text
Image 1 is the owned poster to edit.
Replace only the headline "Create together" with "Crea en equipo".
Replace only the button "Join now" with "Únete ahora".
Keep the photo, logo, palette, grid, prices and dates unchanged.
Allow font-size adjustment only inside the two existing text boxes.
Do not stretch glyphs or translate any other copy.
```

中文审核要点：重音字符不能遗漏；不能把价格、日期一并“本地化”；标题过长时调整字号和换行，不要拉伸字形。必要时在设计工具中排入最终文字。
