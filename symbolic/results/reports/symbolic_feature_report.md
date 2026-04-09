# symbolic 共通テンプレレポート

このレポートは、symbolic 分析の共通テンプレパイプラインから生成されています。

## 概要

- 生成行数: 1
- モード: symbolic 共通テンプレ
- 値の表とは別に、列の意味を読むための特徴量辞書も出力します。
- 次は demo の音符イベント生成部を music21 パーサに差し替える段階です。

## 出力ファイル

- `results/tables/symbolic_feature_table.csv`: 1 曲 1 行の特徴量表
- `results/tables/symbolic_feature_dictionary.csv`: 各列の意味一覧

## 次の段階

- demo 音符イベント生成を music21 ベースのパーサへ差し替える
- 声部進行、調推定、終止候補、反復検出を追加する
- PCA、UMAP、統計検定へつながる分析層を広げる
