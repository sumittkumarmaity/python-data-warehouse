from etl.utils.logger import logger
from etl.utils.sql_runner import run_sql_file

def Load_DTL_DW_HOP_1():
   
    sql_files  = {
        "sql/02_dw_hop1/load_dtl_dw_hop1_customers.sql": 'TBL_DTL_DW_HOP1_Customers',
        "sql/02_dw_hop1/load_dtl_dw_hop1_product_subcategories.sql": 'TBL_DTL_DW_HOP1_Product_Subcategories',
        "sql/02_dw_hop1/load_dtl_dw_hop1_product_categories.sql": 'TBL_DTL_DW_HOP1_Product_Categories',
        "sql/02_dw_hop1/load_dtl_dw_hop1_products.sql": 'TBL_DTL_DW_HOP1_Products',
        "sql/02_dw_hop1/load_dtl_dw_hop1_territory.sql": 'TBL_DTL_DW_HOP1_Territory',
        "sql/02_dw_hop1/load_dtl_dw_hop1_sales.sql": 'TBL_DTL_DW_HOP1_Sales'
    }

    try:
        for file, table in sql_files.items():
            print(f"Loading... {table} Data using : {file}")
            logger.info(f"Loading... {table} Data using : {file}")
            run_sql_file(file)

        logger.info(f"Data successfully loaded into HOP-1 layer.")
    except Exception as e:
        logger.error(f"Error executing SQL script: {e}")
        raise
    finally:
        logger.info(f"HOP-1 Data Load Process Completed.")