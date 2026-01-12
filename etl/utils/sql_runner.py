from config.db_connection import get_connection
from etl.utils.logger import logger

def run_sql_file(path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    try:
        # IMPORTANT: multi=True prevents Python crash
        for result in cursor.execute(sql_script, multi=True):
            pass

        conn.commit()
        logger.info(f"Executed SQL file successfully: {path}")

    except Exception as e:
        conn.rollback()
        logger.error(f"Error executing SQL file {path}: {e}")
        raise

    finally:
        cursor.close()
        conn.close()
