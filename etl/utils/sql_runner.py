from config.db_connection import get_connection
from etl.utils.logger import logger

# Function to run SQL script from a file
def run_sql_file(path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    try:
        # IMPORTANT: multi=True prevents Python crash
        for result in cursor.execute(sql_script, multi=True):
            # print(f"Running query: {result.statement}")
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

# Function to automatically generate tables by executing multiple SQL scripts
def SQL_Auto_Table_Generator():
    sql_files = [
        "sql/01_staging/create_staging_tables.sql",
        "sql/01_staging/insert_sales_years.sql",
        "sql/02_dw_hop1/create_dw_hop1_tables.sql",
        "sql/03_dw_hop2/create_dw_hop2_tables.sql",
        "sql/04_data_mart/create_data_mart_tables.sql",
        "sql/05_views/vw_customer_retention.sql",
        "sql/05_views/vw_customer_clv.sql",
        "sql/06_logs/create_logs_table.sql"
    ]

    try:
        for sql in sql_files:
            print(f"Creating... Script from File: {sql}")
            logger.info(f"Creating... Script from File: {sql}")
            run_sql_file(sql)

        logger.info(f"Executed SQL script successfully.")
    except Exception as e:
        logger.error(f"Error executing SQL script: {e}")
        raise
    finally:
        logger.info(f"Executed SQL script successfully.")