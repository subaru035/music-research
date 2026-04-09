from dataclasses import dataclass


@dataclass(frozen=True)
class SymbolicElement:
    internal_name: str
    display_name_ja: str
    layer_ja: str
    available_in: tuple[str, ...]
    unit_of_analysis: str
    feature_examples_ja: tuple[str, ...]
    extraction_route_ja: str


SYMBOLIC_ONTOLOGY: tuple[SymbolicElement, ...] = (
    SymbolicElement(
        internal_name="note_rest_event",
        display_name_ja="音符・休符イベント",
        layer_ja="記載済み要素",
        available_in=("MIDI", "MusicXML"),
        unit_of_analysis="event",
        feature_examples_ja=("音符数", "休符数", "平均音価"),
        extraction_route_ja="パースした楽譜からイベント列を順番に並べます。",
    ),
    SymbolicElement(
        internal_name="onset_duration",
        display_name_ja="開始位置と音価",
        layer_ja="記載済み要素",
        available_in=("MIDI", "MusicXML"),
        unit_of_analysis="event",
        feature_examples_ja=("音符密度", "音価エントロピー", "休符比率"),
        extraction_route_ja="各音の onset と duration を読み取り、小節または曲全体に集約します。",
    ),
    SymbolicElement(
        internal_name="part_voice_assignment",
        display_name_ja="パート・声部割当",
        layer_ja="記載済み要素",
        available_in=("MIDI", "MusicXML"),
        unit_of_analysis="part",
        feature_examples_ja=("パート数", "平均発声音部数"),
        extraction_route_ja="イベント列を part_id ごとにまとめて声部系列を作ります。",
    ),
    SymbolicElement(
        internal_name="pitch_sequence",
        display_name_ja="音高系列",
        layer_ja="導出要素",
        available_in=("MIDI", "MusicXML"),
        unit_of_analysis="part",
        feature_examples_ja=("全体音域", "主旋律平均音程幅", "主旋律順次進行率"),
        extraction_route_ja="各パート内で onset 順に並べ、隣接音高差を計算します。",
    ),
    SymbolicElement(
        internal_name="vertical_slice",
        display_name_ja="同時発音スライス",
        layer_ja="導出要素",
        available_in=("MIDI", "MusicXML"),
        unit_of_analysis="onset",
        feature_examples_ja=("同時発音率", "平均発声音部数", "最大発声音部数"),
        extraction_route_ja="同じ onset の音をまとめて垂直断面を作ります。",
    ),
    SymbolicElement(
        internal_name="pitch_class_profile",
        display_name_ja="ピッチクラス分布",
        layer_ja="推定要素の前段階",
        available_in=("MIDI", "MusicXML"),
        unit_of_analysis="piece",
        feature_examples_ja=("ピッチクラス種類数", "調推定"),
        extraction_route_ja="pitch を pitch class に落として分布を作ります。",
    ),
)


def ontology_by_layer() -> dict[str, list[SymbolicElement]]:
    grouped: dict[str, list[SymbolicElement]] = {}
    for element in SYMBOLIC_ONTOLOGY:
        grouped.setdefault(element.layer_ja, []).append(element)
    return grouped
