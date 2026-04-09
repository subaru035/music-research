# music-research

記譜ベース分析と音源ベース分析を、意図的に分離して進めるための親ワークスペースです。

- `symbolic/`: MIDI、MusicXML などの楽譜的データを扱うプロジェクト
- `audio/`: wav、mp3 などの録音音源を扱うプロジェクト

親ディレクトリでは、次のような軽い共有物だけを管理します。

- 研究メモ
- 比較観点
- 結果の見方や解釈ルール

コード、依存環境、特徴量設計は各子プロジェクト側で分離して保持します。

## 構成

```text
music-research/
  README.md
  docs/
    theme-notes/
    papers/
    feature-catalogs/
    meeting-notes/
  symbolic/
  audio/
```

## 共有ドキュメント

- `docs/theme-notes/`: 研究テーマ全体の整理
- `docs/papers/`: 論文メモや読書メモ
- `docs/feature-catalogs/`: 両プロジェクトで共有したい特徴量の棚卸し
- `docs/meeting-notes/`: 打ち合わせや意思決定の記録

## クイックスタート

`symbolic` と `audio` は独立して開発できます。

### symbolic プロトタイプ

```powershell
Set-Location .\symbolic
$env:PYTHONPATH = "src"
python -m symbolic_lab
```

### audio プロトタイプ

```powershell
Set-Location .\audio
$env:PYTHONPATH = "src"
python -m audio_lab
```

どちらも `results/` 配下に、特徴量 CSV と簡単なレポートを出力します。
