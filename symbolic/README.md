# symbolic

楽譜・記譜データを対象にした音楽分析プロジェクトです。

## 目的

次のような研究に使える、再利用可能な特徴量抽出・分析基盤を作ることを目指します。

- 作曲者らしさの分析
- 時代様式の比較
- バッハ・コラールなどの構造分析
- 音楽理論と結びついた解釈

## 現在のスコープ

- 当面は `music21` を中心にした symbolic 解析を想定
- まずは MIDI / MusicXML を共通ルートに流せる土台を整える
- 音楽生成は扱わない
- 深層学習は主題にしない

## 入力

- MIDI
- MusicXML
- 必要に応じてその他の楽譜由来データ

## 出力

- 1 曲 1 行の特徴量表
- 各列の意味を確認するための特徴量辞書
- 分布確認や比較のための集計結果
- 将来的な PCA、UMAP、分類補助の土台
- 再利用可能な抽出パイプライン

## 現在のテンプレ

この雛形には次のものが入っています。

- プロジェクト専用のパッケージ構成
- `symbolic` の構成要素 ontology
- 音符イベント列へ正規化するための中間表現
- 声部系列、onset スライス、調性前段階などの派生ビュー
- 汎用特徴量ファミリのテンプレ実装
- `data/raw/` を走査する最小 CLI
- 日本語ラベルの特徴量表出力
- 列の意味を読むための特徴量辞書出力
- 簡易レポート生成

今の段階では、「どの `symbolic` 研究でも流用できる共通テンプレルート」を
先に固めています。バッハ・コラール専用の分析ではなく、
今後どの MIDI / MusicXML データへも載せ替えやすい形を優先しています。

関連ファイル:

- `../docs/feature-catalogs/symbolic-features.md`
- `../docs/feature-catalogs/symbolic-template-ja.md`
- `src/symbolic_lab/features/ontology.py`
- `src/symbolic_lab/features/context.py`
- `src/symbolic_lab/features/catalog.py`

## クイックスタート

```powershell
Set-Location .\symbolic
$env:PYTHONPATH = "src"
python -m symbolic_lab
```

生成されるファイル:

- `results/tables/symbolic_feature_table.csv`
- `results/tables/symbolic_feature_dictionary.csv`
- `results/reports/symbolic_feature_report.md`
