"""
pytest test suite for the employee_events Python package.

Run:
    pytest tests/ -v
"""

import sqlite3
import pytest
from pathlib import Path

# ── Path to the SQLite database ───────────────────────────────────────────────
DB_PATH: Path = (
    Path(__file__).parent.parent
    / "python-package"
    / "employee_events"
    / "employee_events.db"
)


# ── Fixture ───────────────────────────────────────────────────────────────────

@pytest.fixture
def db_path() -> Path:
    """Returns the Path to employee_events.db."""
    return DB_PATH


# ── Helper ────────────────────────────────────────────────────────────────────

def _table_exists(db: Path, table_name: str) -> bool:
    conn   = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,),
    )
    result = cursor.fetchone()
    conn.close()
    return result is not None


# ── Tests ─────────────────────────────────────────────────────────────────────

def test_db_exists(db_path):
    """The SQLite database file must exist on disk."""
    assert db_path.exists(), f"Database not found at {db_path}"


def test_employee_table_exists(db_path):
    """The 'employee' table must be present in the database."""
    assert _table_exists(db_path, "employee"), "Table 'employee' not found"


def test_team_table_exists(db_path):
    """The 'team' table must be present in the database."""
    assert _table_exists(db_path, "team"), "Table 'team' not found"


def test_employee_events_table_exists(db_path):
    """The 'employee_events' table must be present in the database."""
    assert _table_exists(db_path, "employee_events"), "Table 'employee_events' not found"
