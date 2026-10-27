from app.database import get_connection, init_db


def test_init_db_cria_tabelas(tmp_path, monkeypatch):
    # Redireciona o banco para uma pasta temporária, para não afetar o app.db real
    from app import database
    monkeypatch.setattr(database, "DB_PATH", tmp_path / "test.db")

    init_db()

    with get_connection() as conn:
        tabelas = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        nomes = [t["name"] for t in tabelas]

    assert "users" in nomes
    assert "cases" in nomes
    assert "case_actions" in nomes
    assert "data_imports" in nomes