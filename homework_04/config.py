import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd@localhost/blog"
DB_ECHO = False
