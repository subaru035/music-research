from pathlib import Path


def build_audio_feature_row(track_path: Path) -> dict[str, float | str]:
    name = track_path.stem or "unknown_track"
    return {
        "track_id": name,
        "source_name": track_path.name,
        "tempo_estimate": 128.0,
        "onset_density": 3.2,
        "spectral_centroid_mean": 2460.0,
        "spectral_bandwidth_mean": 1890.0,
        "mfcc_1_mean": -142.0,
        "rms_energy_mean": 0.18,
        "structure_novelty_peak_count": 5.0,
    }

