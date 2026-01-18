from etl.utils.logger import logger
from etl.utils.sql_runner import run_sql_file

# Function to load detailed data into HOP-2 layer
def Load_DTL_DW_HOP_2():
   
    sql_files  = {
        "sql/03_dw_hop2/load_dtl_dw_hop2_customers.sql": 'TBL_DTL_DW_HOP2_Customers',
        "sql/03_dw_hop2/load_dtl_dw_hop2_sales.sql": 'TBL_DTL_DW_HOP2_Sales'
    }

    try:
        for file, table in sql_files.items():
            print(f"Loading... {table} Data using : {file}")
            logger.info(f"Loading... {table} Data using : {file}")
            run_sql_file(file)

        logger.info(f"Data successfully loaded into HOP-2 layer.")
    except Exception as e:
        logger.error(f"Error executing SQL script: {e}")
        raise
    finally:
        logger.info(f"HOP-2 Data Load Process Completed.")