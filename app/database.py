import sqlite3
from pathlib import Path

# Caminho do arquivo do banco, na raiz do projeto
BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "app.db"
SCHEMA_PATH = BASE_DIR / "docs" / "schema.sql"


def get_connection() -> sqlite3.Connection:
    """Abre uma conexão com o SQLite e permite acessar colunas pelo nome."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db() -> None:
    """Cria as tabelas a partir do schema.sql, se ainda não existirem."""
    schema = SCHEMA_PATH.read_text(encoding="utf-8")
    with get_connection() as conn:
        conn.executescript(schema)