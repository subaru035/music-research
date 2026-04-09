from collections import Counter
from math import log2, sqrt
from pathlib import Path

from symbolic_lab.features.context import build_analysis_context, build_demo_note_events
from symbolic_lab.models import AnalysisContext, FeatureSpec, NoteEvent


def entropy(values: tuple[float, ...]) -> float:
    counts = Counter(values)
    total = len(values)
    if total == 0:
        return 0.0
    return -sum((count / total) * log2(count / total) for count in counts.values())


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def population_std(values: list[float]) -> float:
    if not values:
        return 0.0
    center = mean(values)
    return sqrt(sum((value - center) ** 2 for value in values) / len(values))


def melody_intervals(notes: tuple[NoteEvent, ...]) -> list[int]:
    if len(notes) < 2:
        return []
    return [
        abs(current.pitch - previous.pitch)
        for previous, current in zip(notes, notes[1:])
    ]


def step_ratio(intervals: list[int]) -> float:
    if not intervals:
        return 0.0
    return sum(1 for interval in intervals if interval <= 2) / len(intervals)


def pitch_range(notes: tuple[NoteEvent, ...]) -> float:
    if not notes:
        return 0.0
    pitches = [note.pitch for note in notes]
    return float(max(pitches) - min(pitches))


def mean_active_voices(context: AnalysisContext) -> float:
    if not context.onset_slices:
        return 0.0
    counts = [len(notes) for notes in context.onset_slices.values()]
    return mean([float(count) for count in counts])


def max_active_voices(context: AnalysisContext) -> float:
    if not context.onset_slices:
        return 0.0
    return float(max(len(notes) for notes in context.onset_slices.values()))


def simultaneity_ratio(context: AnalysisContext) -> float:
    if not context.onset_slices:
        return 0.0
    simultaneous = sum(1 for notes in context.onset_slices.values() if len(notes) > 1)
    return simultaneous / len(context.onset_slices)


def note_density(context: AnalysisContext) -> float:
    if context.piece_duration == 0:
        return 0.0
    return len(context.notes) / context.piece_duration


def build_internal_feature_values(context: AnalysisContext) -> dict[str, float | str]:
    all_pitches = [float(note.pitch) for note in context.notes]
    soprano = context.part_sequences.get("soprano", tuple())
    intervals = melody_intervals(soprano)

    return {
        "piece_id": context.piece_id,
        "source_name": context.source_name,
        "feature_source": context.feature_source,
        "event_note_count": float(len(context.notes)),
        "voice_part_count": float(len(context.part_sequences)),
        "pitch_overall_range": pitch_range(context.notes),
        "pitch_mean": mean(all_pitches),
        "pitch_std": population_std(all_pitches),
        "melody_pitch_range": pitch_range(soprano),
        "melody_mean_interval": mean([float(interval) for interval in intervals]),
        "melody_step_ratio": step_ratio(intervals),
        "rhythm_note_density": note_density(context),
        "rhythm_mean_duration": mean([float(duration) for duration in context.durations]),
        "rhythm_duration_entropy": entropy(context.durations),
        "vertical_onset_count": float(len(context.onset_slices)),
        "vertical_simultaneity_ratio": simultaneity_ratio(context),
        "texture_mean_active_voices": mean_active_voices(context),
        "texture_max_active_voices": max_active_voices(context),
        "tonality_pitch_class_variety": float(len(context.pitch_classes)),
    }


FEATURE_SPECS: tuple[FeatureSpec, ...] = (
    FeatureSpec("piece_id", "曲ID", "識別", "記載済み", "piece", "text", "曲ごとの識別子です。", "入力ファイル名などから安定した ID を作ります。"),
    FeatureSpec("source_name", "元ファイル名", "識別", "記載済み", "piece", "text", "入力に使った元ファイル名です。", "読み込んだファイルの名前をそのまま保持します。"),
    FeatureSpec("feature_source", "特徴量ソース", "識別", "記載済み", "piece", "text", "どの抽出系で作られた特徴量行かを示します。", "demo か music21 実装かなどの系統を記録します。"),
    FeatureSpec("event_note_count", "音符数", "イベント", "記載済み", "piece", "count", "曲に含まれる音符イベントの総数です。", "正規化済み音符イベント列の長さを数えます。"),
    FeatureSpec("voice_part_count", "パート数", "声部", "記載済み", "piece", "count", "曲内で区別されたパートや声部の数です。", "part_id の種類数を数えます。"),
    FeatureSpec("pitch_overall_range", "全体音域", "音高", "導出", "piece", "semitone", "曲全体の最高音と最低音の差です。", "全音符の pitch から max - min を取ります。"),
    FeatureSpec("pitch_mean", "平均音高", "音高", "導出", "piece", "midi_pitch", "曲全体での音高平均です。", "全音符の pitch の平均を取ります。"),
    FeatureSpec("pitch_std", "音高ばらつき", "音高", "導出", "piece", "midi_pitch", "音高の散らばり具合です。", "全音符の pitch の標準偏差を計算します。"),
    FeatureSpec("melody_pitch_range", "主旋律音域", "旋律", "導出", "part", "semitone", "主旋律系列の最高音と最低音の差です。", "現行テンプレでは soprano パートを主旋律として計算します。"),
    FeatureSpec("melody_mean_interval", "主旋律平均音程幅", "旋律", "導出", "part", "semitone", "主旋律の隣接音どうしの平均距離です。", "主旋律系列の隣接 pitch 差の絶対値平均を取ります。"),
    FeatureSpec("melody_step_ratio", "主旋律順次進行率", "旋律", "導出", "part", "ratio", "主旋律で 2 半音以内の進行が占める割合です。", "隣接音程のうち 2 半音以内の件数比率を計算します。"),
    FeatureSpec("rhythm_note_density", "音符密度", "リズム", "導出", "piece", "notes_per_time", "単位時間あたりの音符数です。", "音符数を曲長で割ります。"),
    FeatureSpec("rhythm_mean_duration", "平均音価", "リズム", "導出", "piece", "duration_unit", "音価の平均です。", "全音符の duration の平均を取ります。"),
    FeatureSpec("rhythm_duration_entropy", "音価エントロピー", "リズム", "導出", "piece", "entropy", "音価の種類の多様さです。", "音価分布の Shannon entropy を計算します。"),
    FeatureSpec("vertical_onset_count", "発音開始点数", "垂直性", "導出", "piece", "count", "異なる onset の数です。", "onset ごとにまとめたスライス数を数えます。"),
    FeatureSpec("vertical_simultaneity_ratio", "同時発音率", "垂直性", "導出", "onset", "ratio", "2 音以上が同時に鳴る onset の割合です。", "onset スライスのうち複数音を含むものの比率を取ります。"),
    FeatureSpec("texture_mean_active_voices", "平均発声音部数", "テクスチャ", "導出", "onset", "count", "1 onset あたり平均で何声部鳴るかです。", "各 onset の発声音数を平均します。"),
    FeatureSpec("texture_max_active_voices", "最大発声音部数", "テクスチャ", "導出", "onset", "count", "同時に鳴った声部数の最大値です。", "各 onset の発声音数の最大を取ります。"),
    FeatureSpec("tonality_pitch_class_variety", "ピッチクラス種類数", "調性", "推定前段階", "piece", "count", "12 音クラス上で使われた種類数です。", "pitch % 12 の種類数を数えます。"),
)


def build_feature_dictionary_rows() -> list[dict[str, str]]:
    return [
        {
            "列名": spec.label_ja,
            "内部キー": spec.internal_key,
            "領域": spec.domain,
            "層": spec.layer,
            "観測単位": spec.observation_unit,
            "単位": spec.value_unit,
            "意味": spec.description_ja,
            "計算ルート": spec.route_ja,
        }
        for spec in FEATURE_SPECS
    ]


def to_display_row(internal_values: dict[str, float | str]) -> dict[str, float | str]:
    row: dict[str, float | str] = {}
    for spec in FEATURE_SPECS:
        row[spec.label_ja] = internal_values[spec.internal_key]
    return row


def build_feature_row_from_notes(
    piece_id: str,
    source_name: str,
    notes: tuple[NoteEvent, ...],
) -> dict[str, float | str]:
    context = build_analysis_context(piece_id=piece_id, source_name=source_name, notes=notes)
    internal_values = build_internal_feature_values(context)
    return to_display_row(internal_values)


def build_symbolic_feature_row(piece_path: Path) -> dict[str, float | str]:
    name = piece_path.stem or "unknown_piece"
    notes = build_demo_note_events()
    return build_feature_row_from_notes(
        piece_id=name,
        source_name=piece_path.name,
        notes=notes,
    )
