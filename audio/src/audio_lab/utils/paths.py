from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = PACKAGE_ROOT.parents[1]


def raw_data_dir() -> Path:
    return PROJECT_ROOT / "data" / "raw"


def results_tables_dir() -> Path:
    return PROJECT_ROOT / "results" / "tables"


def results_reports_dir() -> Path:
    return PROJECT_ROOT / "results" / "reports"

