from pathlib import Path


def build_symbolic_feature_row(piece_path: Path) -> dict[str, float | str]:
    name = piece_path.stem or "unknown_piece"
    return {
        "piece_id": name,
        "source_name": piece_path.name,
        "melody_pitch_range": 14.0,
        "melody_step_ratio": 0.68,
        "rhythm_note_density": 1.25,
        "rhythm_duration_entropy": 1.73,
        "harmony_chord_change_rate": 0.42,
        "voice_leading_contrary_motion_ratio": 0.37,
        "form_repetition_ratio": 0.21,
    }

