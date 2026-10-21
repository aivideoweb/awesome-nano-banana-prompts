# Awesome Nano Banana 2.1 Prompts — 日本語ガイド

**[aivideoweb.com チーム](https://aivideoweb.com)** が制作・管理する、独立したオープンソースの画像プロンプト集です。商品写真、広告、教材、人物、絵コンテ、画像編集など、日常の制作課題から探せます。

[English](README.md) · [简体中文](README_zh.md) · [日本語](README_ja.md) · [Español](README_es.md)

![aivideoweb.com オリジナルカバー](assets/images/cover.webp)

## 収録内容

48 の独立したシナリオを 12 カテゴリに整理しています。全プロンプトに英語版と簡体字中国語版があり、構図、正確な文字列、制約、確認項目を含みます。**この日本語ページは導入ガイドとサンプルであり、48 件すべての日本語訳ではありません。**

掲載画像は内蔵 imagegen ツールで新しく生成した説明用の作例です。Nano Banana 2.1 の実測結果ではありません。対象モデルでのテスト状況はすべて `not_tested` です。[画像生成記録](assets/generation-manifest.json)で実際の生成方法を確認できます。

## 使い方

1. [英語カタログ](prompts/en.md)または[中国語カタログ](prompts/zh.md)から目的に近いシナリオを選びます。
2. 架空の商品や色を自分の企画に置き換え、画像内に表示する文言を正確に指定します。
3. 使用ツールでモデル、縦横比、解像度を選びます。プロンプトに比率を書くだけでは設定されません。
4. 編集では、使用権限のある参考画像をアップロードし、各画像の役割を明記します。
5. 小さな下書きから始め、確認項目を見ながら一度に一つの問題を修正します。

## 日本語のスターター例

```text
用途：架空の小さな書店の開店ポスター。
画面：クリーム色の紙に、暖かな光が漏れる小さな青い扉。
扉の左右に高さの異なる本を配置。紙の質感を残す。
上部に読みやすい濃紺の見出しを置く。
正確な文字：「本と出会う週末」
追加の文字、著者名、価格、ロゴ、透かしは入れない。
確認：見出しの文字、扉の形、本の重なりを確認する。
```

文字化けや不自然な改行がないか、出力画像そのものを確認してください。必要なら最終文字組みをデザインツールで整えます。

## おすすめの入口

| 目的 | レシピ |
|---|---|
| 商品写真 | [Ceramic travel mug](site/prompts/ceramic-travel-mug.html) |
| 広告ポスター | [Coffee launch](site/prompts/coffee-launch.html) |
| 教材 | [Plant growth](site/prompts/plant-cycle.html) |
| 絵コンテ | [Fox courier](site/prompts/fox-courier.html) |
| 局所編集 | [Wardrobe edit](site/prompts/wardrobe-edit.html) |

## ローカルで見る

リポジトリのルートで `python3 -m http.server 8000` を実行し、`http://localhost:8000/site/` を開きます。[公開ガイド](docs/publishing.md)にホスティング時の注意点があります。

原文とコードは [MIT](LICENSE) です。画像の扱いは[アセット説明](assets/README.md)をご確認ください。商用利用の適合性や第三者の権利処理を保証するものではありません。

翻訳や実モデルのテストに参加する場合は、[貢献ガイド](CONTRIBUTING.md)をご覧ください。完全版の翻訳と部分的な導入ガイドを区別して公開します。
