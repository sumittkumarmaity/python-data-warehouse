
from etl.utils.db_initializer import Create_Database_if_not_Exists
from etl.utils.sql_runner import SQL_Auto_Table_Generator
from etl.load.load_master_data import Load_Master_Data
from etl.load.load_sales import Load_Sales_Data
from etl.transform.staging_to_hop1 import Load_DTL_DW_HOP_1
from etl.transform.hop1_to_hop2 import Load_DTL_DW_HOP_2
from etl.transform.hop_to_datamart import Load_FL_Data_Mart

print("================================================================")
print("ETL :: PIPELINE STARTED")
print("================================================================")
# STEP 0: Ensure DB Exists
Create_Database_if_not_Exists()
print("Database Ready.")

# STEP 1: Run SQL Scripts
print("ETL :: Initialization :: Script Generation Started ...")
print("================================================================")
SQL_Auto_Table_Generator()
print("ETL :: Initialization :: Script Generation Completed.")

# STEP 2: Load Master Data
print("ETL :: LOADING MASTER DATA")
Load_Master_Data()

# STEP 3: Load Sales Data
print("ETL :: LOADING SALES DATA")
Load_Sales_Data()

# STEP 4: Transform Layers
print("ETL :: Data Transformation Layer ​:: Data Warehouse ")
print("================================================================")
# STEP 4.1: Load HOP-1 Data
print("ETL :: LOADING HOP-1 DATA")
Load_DTL_DW_HOP_1()

# STEP 4.2: Load HOP-2 Data
print("ETL :: LOADING HOP-2 DATA")
# Load_DTL_DW_HOP_2()

# STEP 5: Load Data-Mart/Final Layer
print("ETL :: LOADING DATA-MART/FINAL LAYER DATA")
# Load_FL_Data_Mart()

print("================================================================")
print("ETL :: PIPELINE COMPLETED SUCCESSFULLY !! ")
print("================================================================")

# Optional: Prompt for Report Generation 
# user_input = input("Do you want to generate reports ? (yes/no): ").strip().lower()

# if user_input in ("yes", "y"):
#     print("[REPORT] Launching Dashboard...")
    