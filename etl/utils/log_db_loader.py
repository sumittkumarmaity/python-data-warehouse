from config.db_connection import get_connection
from datetime import datetime
import os

def Load_Logs_to_DB():
    """
    Reads ETL log file and inserts logs into ETL_EXECUTION_LOGS table
    """
    log_file_path  = os.path.join('logs', 'etl_execution.log')
    conn = get_connection()
    cursor = conn.cursor()

    insert_sql = """
        INSERT INTO ETL_EXECUTION_LOGS
        (LogDateTime, LogType, LogMessage)
        VALUES (%s, %s, %s)
    """
    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or "||" not in line:
                continue

            try:
                datetime_part, log_type, message = line.split("||")
                log_datetime = datetime.strptime(
                    datetime_part.strip(), "%Y-%m-%d %H:%M:%S,%f"
                )
                log_type = log_type.strip()
                message = message.strip()

                cursor.execute(
                    insert_sql,
                    (log_datetime, log_type, message)
                )

            except Exception as e:
                print(f"[LOG LOAD WARNING] Skipped line: {line}")

    conn.commit()
    cursor.close()
    conn.close()
