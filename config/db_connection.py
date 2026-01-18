import mysql.connector
from config.env_loader import get_env
from sqlalchemy import create_engine

# Database Server connection #
def get_server_connection():
    """Connect without selecting a database"""
    return mysql.connector.connect(
        host=get_env("DB_HOST"),
        port=int(get_env("DB_PORT")),
        user=get_env("DB_USER"),
        password=get_env("DB_PASSWORD"),
        autocommit=False
    )

# Database connection #
def get_connection():
    """Connect to specific database"""
    return mysql.connector.connect(
        host=get_env("DB_HOST"),
        port=int(get_env("DB_PORT")),
        user=get_env("DB_USER"),
        password=get_env("DB_PASSWORD"),
        database=get_env("DB_NAME"),
        autocommit=False
    )

# Spacialy for SQL Lite #
def get_engine():
    user = get_env("DB_USER")
    password = get_env("DB_PASSWORD")
    host = get_env("DB_HOST")
    port = get_env("DB_PORT")
    database = get_env("DB_NAME")
    connection_url = (
        f"mysql+mysqlconnector://{user}:{password}"
        f"@{host}:{port}/{database}"
    )
    engine = create_engine(connection_url)
    return engine

