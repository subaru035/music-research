from dataclasses import dataclass


@dataclass(frozen=True)
class NoteEvent:
    part_id: str
    pitch: int
    onset: float
    duration: float


@dataclass(frozen=True)
class AnalysisContext:
    piece_id: str
    source_name: str
    feature_source: str
    notes: tuple[NoteEvent, ...]
    part_sequences: dict[str, tuple[NoteEvent, ...]]
    onset_slices: dict[float, tuple[NoteEvent, ...]]
    pitch_classes: tuple[int, ...]
    durations: tuple[float, ...]
    piece_duration: float


@dataclass(frozen=True)
class FeatureSpec:
    internal_key: str
    label_ja: str
    domain: str
    layer: str
    observation_unit: str
    value_unit: str
    description_ja: str
    route_ja: str
