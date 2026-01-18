from etl.extract.csv_reader import read_csv
from etl.load.load_staging import load_dataframe
from etl.utils.logger import logger

# Function to load master data from CSV files into staging tables
def Load_Master_Data():
    master_files = {
        "Customers.csv": "TBL_Staging_Customers",
        "Products.csv": "TBL_Staging_Products",
        "Product_Categories.csv": "TBL_Staging_Product_Categories",
        "Product_Subcategories.csv": "TBL_Staging_Product_Subcategories",
        "Territory.csv": "TBL_Staging_Territory"
    }

    logger.info(f"ETL :: LOADING MASTER DATA [CUSTOMERS, PRODUCTS, PRODUCT_CATEGORIES, TERRITORY]")
    for csv, table in master_files.items():
        print(f"Loading Master Data from files ('{csv}') to table ('{table}')...")
        logger.info(f"Loading Master Data from files ('{csv}') to table ('{table}')...")
        df = read_csv(csv)
        load_dataframe(table, df)
