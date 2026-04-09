from pytest import approx

from symbolic_lab.features.catalog import build_feature_dictionary_rows, build_feature_row_from_notes
from symbolic_lab.features.context import build_demo_note_events
from symbolic_lab.features.ontology import SYMBOLIC_ONTOLOGY, ontology_by_layer


def test_build_feature_row_from_demo_note_events() -> None:
    row = build_feature_row_from_notes(
        piece_id="demo",
        source_name="demo.musicxml",
        notes=build_demo_note_events(),
    )
    assert row["音符数"] == 16.0
    assert row["パート数"] == 4.0
    assert row["主旋律音域"] == 5.0
    assert row["主旋律平均音程幅"] == approx(5.0 / 3.0)
    assert row["主旋律順次進行率"] == 1.0
    assert row["音符密度"] == 3.2
    assert row["同時発音率"] == 1.0
    assert row["平均発声音部数"] == 4.0
    assert row["ピッチクラス種類数"] == 7.0


def test_symbolic_ontology_groups_by_layer() -> None:
    grouped = ontology_by_layer()
    assert SYMBOLIC_ONTOLOGY
    assert "記載済み要素" in grouped
    assert "導出要素" in grouped
    assert "推定要素の前段階" in grouped


def test_feature_dictionary_uses_japanese_labels() -> None:
    rows = build_feature_dictionary_rows()
    assert rows
    first = rows[0]
    assert "列名" in first
    assert "意味" in first
    assert any(row["列名"] == "主旋律音域" for row in rows)
