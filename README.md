# music-research

Shared parent workspace for two related but intentionally separated projects:

- `symbolic/` for score-oriented analysis based on MIDI, MusicXML, and other notation-derived data.
- `audio/` for recording-oriented analysis based on wav, mp3, and similar audio formats.

The parent directory keeps only lightweight shared artifacts:

- research notes
- comparison viewpoints
- interpretation rules for results

Code, dependencies, and feature engineering stay project-local on purpose.

## Workspace layout

```text
music-research/
  README.md
  docs/
    theme-notes/
    papers/
    feature-catalogs/
    meeting-notes/
  symbolic/
  audio/
```

## Shared docs

- `docs/theme-notes/` keeps high-level research framing.
- `docs/papers/` keeps paper notes and reading summaries.
- `docs/feature-catalogs/` keeps cross-project feature inventories.
- `docs/meeting-notes/` keeps decision logs.

## Quick start

Each child project can be developed independently.

### Symbolic prototype

```powershell
Set-Location .\symbolic
$env:PYTHONPATH = "src"
python -m symbolic_lab
```

### Audio prototype

```powershell
Set-Location .\audio
$env:PYTHONPATH = "src"
python -m audio_lab
```

Both prototype commands generate one CSV table and one short markdown report under `results/`.

