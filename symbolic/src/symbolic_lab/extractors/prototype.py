from pathlib import Path

SUPPORTED_SUFFIXES = {".mid", ".midi", ".xml", ".musicxml"}


def discover_symbolic_files(raw_dir: Path) -> list[Path]:
    files = [
        path
        for path in sorted(raw_dir.rglob("*"))
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
    ]
    if files:
        return files
    return [raw_dir / "demo_bach_chorale.musicxml"]

