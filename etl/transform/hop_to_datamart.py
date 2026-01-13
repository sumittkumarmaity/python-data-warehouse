from config.db_connection import get_connection

def Load_FL_Data_Mart():
    conn = get_connection()
    cursor = conn.cursor()
    print(f"Loading Data from  DTL_DW_HOP2 to  DataMart/Final Layer ...")
    cursor.execute("INSERT INTO TBL_FL_DM_Customers SELECT * FROM TBL_DTL_DW_HOP2_Customers")
    cursor.execute("INSERT INTO TBL_FL_DM_Products SELECT * FROM TBL_DTL_DW_HOP1_Products")
    cursor.execute("INSERT INTO TBL_FL_DM_Product_Categories SELECT * FROM TBL_DTL_DW_HOP1_Product_Categories")
    cursor.execute("INSERT INTO TBL_FL_DM_Product_Subcategories SELECT * FROM TBL_DTL_DW_HOP1_Product_Subcategories")
    cursor.execute("INSERT INTO TBL_FL_DM_Territory SELECT * FROM TBL_DTL_DW_HOP1_Territory")
    cursor.execute("INSERT INTO TBL_FL_DM_Sales SELECT * FROM TBL_DTL_DW_HOP2_Sales")
    conn.commit()
    cursor.close()
    conn.close()

