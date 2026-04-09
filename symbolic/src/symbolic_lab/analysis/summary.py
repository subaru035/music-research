def build_symbolic_summary(row_count: int) -> list[str]:
    return [
        f"生成行数: {row_count}",
        "モード: symbolic 共通テンプレ",
        "値の表とは別に、列の意味を読むための特徴量辞書も出力します。",
        "次は demo の音符イベント生成部を music21 パーサに差し替える段階です。",
    ]
