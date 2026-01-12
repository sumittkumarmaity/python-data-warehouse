import sys
from etl.utils.db_initializer import create_database_if_not_exists
from etl.utils.sql_runner import run_sql_file
from etl.extract.csv_reader import read_csv
from etl.load.load_staging import load_dataframe
from etl.load.load_sales import load_sales
from etl.transform.staging_to_hop1 import load_hop1
from etl.transform.hop1_to_hop2 import load_hop2
from etl.transform.hop_to_datamart import load_datamart
from etl.utils.logger import logger
print("================================================================")
print("ETL :: PIPELINE STARTED")
print("================================================================")
# STEP 0: Ensure DB Exists
create_database_if_not_exists()
print("Database Ready.")

# STEP 1: Run SQL Scripts
sql_files = [
    "sql/01_staging/create_staging_tables.sql",
    "sql/01_staging/insert_sales_years.sql",
    "sql/02_dw_hop1/create_dw_hop1_tables.sql",
    "sql/03_dw_hop2/create_dw_hop2_tables.sql",
    "sql/04_data_mart/create_data_mart_tables.sql",
    "sql/05_views/vw_customer_retention.sql",
    "sql/05_views/vw_customer_clv.sql"
]

print("ETL :: Initialization :: Script Generation Started ...")
print("================================================================")
for sql in sql_files:
    print(f"Creating... Script from File: {sql}")
    logger.info(f"Creating... Script from File: {sql}")
    run_sql_file(sql)

# STEP 2: Load Master Data
master_files = {
    "Customers.csv": "staging_Customers",
    "Products.csv": "staging_Products",
    "Product_Categories.csv": "staging_Product_Categories",
    "Product_Subcategories.csv": "staging_Product_Subcategories",
    "Territory.csv": "staging_Territory"
}

print("ETL :: LOADING MASTER DATA [CUSTOMERS, PRODUCTS, PRODUCT_CATEGORIES, TERRITORY]")
logger.info(f"ETL :: LOADING MASTER DATA [CUSTOMERS, PRODUCTS, PRODUCT_CATEGORIES, TERRITORY]")
for csv, table in master_files.items():
    print(f"Loading Master Data from files ('{csv}') to table ('{table}')...")
    logger.info(f"Loading Master Data from files ('{csv}') to table ('{table}')...")
    df = read_csv(csv)
    load_dataframe(table, df)

# STEP 3: Load Sales Data
print("ETL :: LOADING SALES DATA")
load_sales()

# STEP 4: Transform Layers
print("ETL :: Data Transformation Layer ​:: Data Warehouse ")
print("================================================================")
print("ETL :: LOADING HOP-1 DATA")
load_hop1()

print("ETL :: LOADING HOP-2 DATA")
load_hop2()

print("ETL :: LOADING DATA-MART/FINAL LAYER DATA")
load_datamart()
print("================================================================")
print("ETL :: PIPELINE COMPLETED SUCCESSFULLY !! ")
print("================================================================")


user_input = input("Do you want to generate reports ? (yes/no): ").strip().lower()

if user_input in ("yes", "y"):
    print("[REPORT] Launching Dashboard...")
    