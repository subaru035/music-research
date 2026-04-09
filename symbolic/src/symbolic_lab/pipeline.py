import csv
from pathlib import Path

from symbolic_lab.analysis.summary import build_symbolic_summary
from symbolic_lab.extractors.prototype import discover_symbolic_files
from symbolic_lab.features.catalog import build_feature_dictionary_rows, build_symbolic_feature_row
from symbolic_lab.utils.paths import raw_data_dir, results_reports_dir, results_tables_dir


def build_rows() -> list[dict[str, float | str]]:
    raw_dir = raw_data_dir()
    raw_dir.mkdir(parents=True, exist_ok=True)
    files = discover_symbolic_files(raw_dir)
    return [build_symbolic_feature_row(path) for path in files]


def write_table(rows: list[dict[str, float | str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_feature_dictionary(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(rows: list[dict[str, float | str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary_lines = build_symbolic_summary(len(rows))
    content = [
        "# symbolic 共通テンプレレポート",
        "",
        "このレポートは、symbolic 分析の共通テンプレパイプラインから生成されています。",
        "",
        "## 概要",
        "",
    ]
    content.extend([f"- {line}" for line in summary_lines])
    content.extend(
        [
            "",
            "## 出力ファイル",
            "",
            "- `results/tables/symbolic_feature_table.csv`: 1 曲 1 行の特徴量表",
            "- `results/tables/symbolic_feature_dictionary.csv`: 各列の意味一覧",
            "",
            "## 次の段階",
            "",
            "- demo 音符イベント生成を music21 ベースのパーサへ差し替える",
            "- 声部進行、調推定、終止候補、反復検出を追加する",
            "- PCA、UMAP、統計検定へつながる分析層を広げる",
        ]
    )
    output_path.write_text("\n".join(content) + "\n", encoding="utf-8")


def run_prototype() -> dict[str, str]:
    rows = build_rows()
    feature_dictionary_rows = build_feature_dictionary_rows()
    table_path = results_tables_dir() / "symbolic_feature_table.csv"
    dictionary_path = results_tables_dir() / "symbolic_feature_dictionary.csv"
    report_path = results_reports_dir() / "symbolic_feature_report.md"
    write_table(rows, table_path)
    write_feature_dictionary(feature_dictionary_rows, dictionary_path)
    write_report(rows, report_path)
    return {
        "table": str(table_path),
        "dictionary": str(dictionary_path),
        "report": str(report_path),
    }
