from symbolic_lab.pipeline import build_rows


def test_build_rows_returns_expected_columns() -> None:
    rows = build_rows()
    assert rows
    first = rows[0]
    assert "曲ID" in first
    assert "主旋律音域" in first
    assert "同時発音率" in first
    assert "ピッチクラス種類数" in first
