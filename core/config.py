from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = APP_DIR / "data"
EXPORT_DIR = APP_DIR / "exports"
HISTORY_FILE = DATA_DIR / "history.xlsx"


def ensure_dirs() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    EXPORT_DIR.mkdir(exist_ok=True)
