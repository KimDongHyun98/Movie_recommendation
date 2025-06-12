#config.py

import os

SERVER_HOSTNAME = os.getenv("DATABRICKS_SERVER_HOSTNAME", "" )# Databricks 워크스페이스 호스트명
HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH", "/model-serving/endpoint")
DB_HTTP_PATH = os.getenv("DATABRICKS_SQL_HTTP_PATH", "") # Databricks SQL 연결용 HTTP 경로
ACCESS_TOKEN = os.getenv("DATABRICKS_ACCESS_TOKEN", "") # Databricks Personal Access Token
TMDB_ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN", "") # TMDB API Bearer Token