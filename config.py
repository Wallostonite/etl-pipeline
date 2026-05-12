# ================================================================
# config.py — Module 03 Configuration
# ================================================================
# This file reads settings from the .env file.
# It never contains passwords or connection strings directly.
# ================================================================

import os, pathlib, logging
from dotenv import load_dotenv

# Load all variables from .env into the environment
load_dotenv()

# industry settings
INDUSTRY       = os.getenv("INDUSTRY",       "bootcamp_data")

#learner schema
LEARNER_SCHEMA = os.getenv("LEARNER_SCHEMA", "learner_05")

# File paths
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent

# The data/ folder is next to config.py in the project root
DATA_DIR = PROJECT_ROOT / "data"        # /path/to/project/data
RAW_DATA_DIR = DATA_DIR / "raw"         # /path/to/project/data/raw
PROC_DATA_DIR = DATA_DIR / "processed"  # /path/to/project/data/processed

# The actual file paths we will read from and write to
RAW_DATA_PATH = RAW_DATA_DIR / "raw-data.csv"
PROC_DATA_PATH = PROC_DATA_DIR / "processed-data.csv"

# Create directories
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROC_DATA_DIR.mkdir(parents=True, exist_ok=True)

# DB_URL comes entirely from .env — no fallback with credentials here.
# If .env is missing or DB_URL is not set, DB_AVAILABLE will be False
# and the project will tell you clearly what to do.
DB_URL = os.getenv("DB_URL", "")

try:
    from sqlalchemy import create_engine
    engine = create_engine(DB_URL, pool_pre_ping=True)
except Exception as _e:
    engine = None  # No databse -  CSV based pipeline will still work

# Logging setup
def _setup_logger(name: str = "darko") -> logging.Logger:
    """
    Create and configure the project logger.

    This function creates one logger that is reused everywhere.
    All modules import `logger` from config.py:
        from config import logger
        logger.info("Something happened")
    """
    # Get or create a logger with the given name
    # logging.getLogger() returns the same object every time for the same name
    # so all modules share one logger instance
    lgr = logging.getLogger(name)

    # Set the minimum level — messages below INFO are ignored
    lgr.setLevel(logging.INFO)

    # Only add handlers if none exist yet (prevent duplicate log lines)
    if not lgr.handlers:
        # StreamHandler sends log messages to the terminal (stdout)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)

        # Formatter defines what each log line looks like
        # %(asctime)s   → timestamp: 2026-01-15 10:23:01
        # %(levelname)s → severity:  INFO / WARNING / ERROR
        # %(message)s   → your message
        fmt = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(fmt)
        lgr.addHandler(handler)

    return lgr

# Create the shared logger — all modules import this
logger = _setup_logger("darko")

# ── Validation thresholds ─────────────────────────────────────────────
# These numbers define what counts as "acceptable" data quality.
# They are constants — all caps by Python convention — and live here
# so they can be changed in one place.
MAX_NULL_PERCENT      = 50.0   # columns with >50% nulls are flagged CRITICAL
MAX_DUPLICATE_PERCENT = 5.0    # more than 5% duplicate rows is CRITICAL



