from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_DIR = PROJECT_ROOT / "data"
EXTERNAL_DIR = DATA_DIR / "external"
KAGGLE_DIR = EXTERNAL_DIR / "kaggle"

RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROJECT_SCOPE_DIR = INTERIM_DIR / "project_scope"
CURATED_DIR = DATA_DIR / "curated"