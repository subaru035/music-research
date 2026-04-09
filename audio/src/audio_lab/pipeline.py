import csv
from pathlib import Path

from audio_lab.analysis.summary import build_audio_summary
from audio_lab.extractors.prototype import discover_audio_files
from audio_lab.features.catalog import build_audio_feature_row
from audio_lab.utils.paths import raw_data_dir, results_reports_dir, results_tables_dir


def build_rows() -> list[dict[str, float | str]]:
    raw_dir = raw_data_dir()
    raw_dir.mkdir(parents=True, exist_ok=True)
    files = discover_audio_files(raw_dir)
    return [build_audio_feature_row(path) for path in files]


def write_table(rows: list[dict[str, float | str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(rows: list[dict[str, float | str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary_lines = build_audio_summary(len(rows))
    content = [
        "# Audio Prototype Report",
        "",
        "This report was generated from the current prototype pipeline.",
        "",
        "## Summary",
        "",
    ]
    content.extend([f"- {line}" for line in summary_lines])
    content.extend(
        [
            "",
            "## Next steps",
            "",
            "- Replace placeholder feature values with librosa-derived measurements.",
            "- Add clustering and similarity exploration notebooks.",
            "- Extend the analysis layer with PCA, UMAP, and unsupervised evaluation.",
        ]
    )
    output_path.write_text("\n".join(content) + "\n", encoding="utf-8")


def run_prototype() -> dict[str, str]:
    rows = build_rows()
    table_path = results_tables_dir() / "prototype_audio_features.csv"
    report_path = results_reports_dir() / "prototype_audio_report.md"
    write_table(rows, table_path)
    write_report(rows, report_path)
    return {"table": str(table_path), "report": str(report_path)}

