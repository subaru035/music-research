from audio_lab.pipeline import build_rows


def test_build_rows_returns_expected_columns() -> None:
    rows = build_rows()
    assert rows
    first = rows[0]
    assert "track_id" in first
    assert "tempo_estimate" in first
    assert "spectral_centroid_mean" in first
