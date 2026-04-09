from symbolic_lab.pipeline import build_rows


def test_build_rows_returns_expected_columns() -> None:
    rows = build_rows()
    assert rows
    first = rows[0]
    assert "piece_id" in first
    assert "melody_pitch_range" in first
    assert "harmony_chord_change_rate" in first

