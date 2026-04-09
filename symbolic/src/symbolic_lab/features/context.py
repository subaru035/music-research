from collections import defaultdict

from symbolic_lab.models import AnalysisContext, NoteEvent


def build_demo_note_events() -> tuple[NoteEvent, ...]:
    return (
        NoteEvent(part_id="soprano", pitch=67, onset=0.0, duration=1.0),
        NoteEvent(part_id="alto", pitch=64, onset=0.0, duration=1.0),
        NoteEvent(part_id="tenor", pitch=60, onset=0.0, duration=1.0),
        NoteEvent(part_id="bass", pitch=55, onset=0.0, duration=1.0),
        NoteEvent(part_id="soprano", pitch=69, onset=1.0, duration=1.0),
        NoteEvent(part_id="alto", pitch=65, onset=1.0, duration=1.0),
        NoteEvent(part_id="tenor", pitch=62, onset=1.0, duration=1.0),
        NoteEvent(part_id="bass", pitch=57, onset=1.0, duration=1.0),
        NoteEvent(part_id="soprano", pitch=71, onset=2.0, duration=1.0),
        NoteEvent(part_id="alto", pitch=67, onset=2.0, duration=1.0),
        NoteEvent(part_id="tenor", pitch=62, onset=2.0, duration=1.0),
        NoteEvent(part_id="bass", pitch=55, onset=2.0, duration=1.0),
        NoteEvent(part_id="soprano", pitch=72, onset=3.0, duration=2.0),
        NoteEvent(part_id="alto", pitch=67, onset=3.0, duration=2.0),
        NoteEvent(part_id="tenor", pitch=60, onset=3.0, duration=2.0),
        NoteEvent(part_id="bass", pitch=48, onset=3.0, duration=2.0),
    )


def collect_part_sequences(notes: tuple[NoteEvent, ...]) -> dict[str, tuple[NoteEvent, ...]]:
    grouped: dict[str, list[NoteEvent]] = defaultdict(list)
    for note in sorted(notes, key=lambda event: (event.part_id, event.onset, event.pitch)):
        grouped[note.part_id].append(note)
    return {part_id: tuple(events) for part_id, events in grouped.items()}


def collect_onset_slices(notes: tuple[NoteEvent, ...]) -> dict[float, tuple[NoteEvent, ...]]:
    grouped: dict[float, list[NoteEvent]] = defaultdict(list)
    for note in sorted(notes, key=lambda event: (event.onset, event.part_id, event.pitch)):
        grouped[note.onset].append(note)
    return {onset: tuple(events) for onset, events in grouped.items()}


def build_analysis_context(
    piece_id: str,
    source_name: str,
    notes: tuple[NoteEvent, ...],
    feature_source: str = "demo_note_events",
) -> AnalysisContext:
    part_sequences = collect_part_sequences(notes)
    onset_slices = collect_onset_slices(notes)
    pitch_classes = tuple(sorted({note.pitch % 12 for note in notes}))
    durations = tuple(note.duration for note in notes)
    piece_duration = max((note.onset + note.duration for note in notes), default=0.0)
    return AnalysisContext(
        piece_id=piece_id,
        source_name=source_name,
        feature_source=feature_source,
        notes=notes,
        part_sequences=part_sequences,
        onset_slices=onset_slices,
        pitch_classes=pitch_classes,
        durations=durations,
        piece_duration=piece_duration,
    )
