import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(__file__).parent / "employee_events.db"


class QueryMixin:
    """Mixin that opens, queries, closes the SQLite DB and returns data."""

    def pandas_query(self, sql: str) -> pd.DataFrame:
        conn = sqlite3.connect(DB_PATH)
        try:
            result = pd.read_sql_query(sql, conn)
        finally:
            conn.close()
        return result

    def tuple_query(self, sql: str) -> list:
        conn = sqlite3.connect(DB_PATH)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
        finally:
            conn.close()
        return result
