# symbolic

Prototype project for notation-based music analysis.

## Goal

Build a reusable feature-extraction and analysis foundation for:

- composer style analysis
- historical style comparison
- Bach chorale structure analysis
- interpretation aligned with music theory

## Current scope

- focus on `music21`-friendly symbolic workflows later
- validate with existing Bach chorale material first
- no generation
- no deep learning as the main topic

## Input

- MIDI
- MusicXML
- other score-derived symbolic files if needed

## Output

- one-row-per-piece feature tables
- distribution and comparison summaries
- PCA, UMAP, and classification support later
- reusable extraction pipeline

## Prototype status

This scaffold currently provides:

- project-local package structure
- placeholder feature catalog
- a minimal CLI that scans `data/raw/`
- a dummy feature table writer
- a short markdown report generator

The placeholder pipeline is intentionally thin so the real `music21` implementation can replace feature stubs without changing the project layout.

## Quick start

```powershell
Set-Location .\symbolic
$env:PYTHONPATH = "src"
python -m symbolic_lab
```

Generated files:

- `results/tables/prototype_symbolic_features.csv`
- `results/reports/prototype_symbolic_report.md`

