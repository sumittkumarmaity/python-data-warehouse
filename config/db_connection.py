import mysql.connector
from config.env_loader import get_env

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
