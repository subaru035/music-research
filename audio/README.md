# audio

Prototype project for recording-based music analysis.

## Goal

Build a reusable feature-extraction and analysis foundation for:

- clustering songs by sound and mood
- exploring genre and atmosphere
- comparing tracks for mashup compatibility
- investigating Vocaloid-oriented audio patterns

## Current scope

- focus on basic `librosa`-style audio features later
- start with unsupervised exploration
- keep the design usable for both research and hobby workflows
- postpone source separation and large models

## Input

- wav
- mp3
- other common audio formats when needed

## Output

- one-row-per-track acoustic feature tables
- visualization support
- clustering support
- a basis for similarity and compatibility scoring

## Prototype status

This scaffold currently provides:

- project-local package structure
- placeholder acoustic feature catalog
- a minimal CLI that scans `data/raw/`
- a dummy feature table writer
- a short markdown report generator

The placeholder pipeline is intentionally thin so the real `librosa` implementation can replace feature stubs without changing the project layout.

## Quick start

```powershell
Set-Location .\audio
$env:PYTHONPATH = "src"
python -m audio_lab
```

Generated files:

- `results/tables/prototype_audio_features.csv`
- `results/reports/prototype_audio_report.md`

