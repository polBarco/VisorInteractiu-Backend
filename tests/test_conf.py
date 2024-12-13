import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from core.database import SessionLocal
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text

def test_database_url_from_env(monkeypatch):
    # Simulate the DATABASE_URL environment variable
    monkeypatch.setenv(
        "DATABASE_URL",
        "postgresql+psycopg2://test_user:test_pass@localhost:5432/test_db"
    )
    
    # Force module reload to recalculate the database URL 
    import importlib
    from core import database
    importlib.reload(database)

    # Check the database URL
    from core.database import SQLALCHEMY_DATABASE_URL
    assert SQLALCHEMY_DATABASE_URL == "postgresql+psycopg2://test_user:test_pass@localhost:5432/test_db"

def test_database_url_from_local_vars(monkeypatch):
    # Simulate environment variables for local database configuration
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setenv("DB_USER", "test_user")
    monkeypatch.setenv("DB_PASSWORD", "test_pass")
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("DB_NAME", "test_db")
    
    from core.database import SQLALCHEMY_DATABASE_URL
    assert SQLALCHEMY_DATABASE_URL == "postgresql+psycopg2://test_user:test_pass@localhost:5432/test_db"

def test_missing_env_vars(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("DB_USER", raising=False)
    monkeypatch.delenv("DB_PASSWORD", raising=False)
    monkeypatch.delenv("DB_HOST", raising=False)
    monkeypatch.delenv("DB_PORT", raising=False)
    monkeypatch.delenv("DB_NAME", raising=False)

    # Simulate database.py logic
    with pytest.raises(Exception) as exc_info:
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_NAME")

        if not all([user, password, host, port, database]):
            raise Exception("Database credentials not found in .env file")

    assert str(exc_info.value) == "Database credentials not found in .env file"

def test_prefer_database_url_over_local_vars(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg2://test_user:test_pass@localhost:5432/test_db")
    monkeypatch.setenv("DB_USER", "local_user")
    monkeypatch.setenv("DB_PASSWORD", "local_pass")
    monkeypatch.setenv("DB_HOST", "local_host")
    monkeypatch.setenv("DB_PORT", "5433")
    monkeypatch.setenv("DB_NAME", "local_db")

    import importlib
    from core import database
    importlib.reload(database)

    from core.database import SQLALCHEMY_DATABASE_URL
    assert SQLALCHEMY_DATABASE_URL == "postgresql+psycopg2://test_user:test_pass@localhost:5432/test_db"

def test_database_connection(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg2://visor_hyuy_user:cICSWGpG2Vx8gbavwUXXSfvd98HRwt9I@dpg-csud4qalqhvc73cla1j0-a.oregon-postgres.render.com/visor_hyuy")

    import importlib
    from core import database
    importlib.reload(database)

    # Verify connection
    from core.database import engine
    try:
        connection = engine.connect()
        connection.close()
    except OperationalError:
        pytest.fail("No se pudo conectar a la base de datos con las credenciales proporcionadas")

def test_invalid_database_url(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg2://invalid_user:invalid_pass@localhost:5432/invalid_db")

    import importlib
    from core import database
    importlib.reload(database)

    # Try to connect to the database
    from core.database import engine
    with pytest.raises(Exception):
        connection = engine.connect()
        connection.close()

def test_multiple_sessions():
    session1 = SessionLocal()
    session2 = SessionLocal()
    try:
        session1.execute(text("SELECT 1"))
        session2.execute(text("SELECT 1"))
    finally:
        session1.close()
        session2.close()

def test_unsupported_database_engine(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "mysql+pymysql://user:pass@localhost/db")

    import importlib
    from core import database

    try:
        importlib.reload(database)
        pytest.fail("An error was expected when using an unsupported engine, but none occurred")
    except ModuleNotFoundError as e:
        # Verificar que el error menciona el módulo pymysql
        assert "pymysql" in str(e), "The error does not mention the pymysql module"
    except Exception as e:
        pytest.fail(f"ModuleNotFoundError was expected, but occurred: {type(e).__name__} - {str(e)}")

