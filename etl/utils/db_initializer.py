from config.db_connection import get_server_connection
from config.env_loader import get_env
from etl.utils.logger import logger
import mysql.connector

# Function to create the database if it does not exist
def Create_Database_if_not_Exists():
    db_name = get_env("DB_NAME")
    logger.info(f"Ensuring database '{db_name}' exists...")
    conn = None
    cursor = None

    try:
        logger.info("Checking database existence...")
        # Connect WITHOUT database
        conn = get_server_connection()
        # print("Connected to MySQL server.", conn)
        cursor = conn.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cursor.execute(f"CREATE DATABASE {db_name}")
        # cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        conn.commit()
        logger.info(f"Database ready: {db_name}")

    except mysql.connector.Error as err:
        if conn:
            conn.rollback()
        logger.error(f"MySQL error while creating database: {err}")
        raise

    except Exception as ex:
        if conn:
            conn.rollback()
        logger.error(f"Unexpected error in DB initializer: {ex}")
        raise

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
