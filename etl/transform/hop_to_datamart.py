from config.db_connection import get_connection

def load_datamart():
    conn = get_connection()
    cursor = conn.cursor()
    print(f"Loading Data from  DTL_DW_HOP2 to  DataMart/Final Layer ...")
    cursor.execute("INSERT INTO FL_DM_Customers SELECT * FROM DTL_DW_HOP2_Customers")
    cursor.execute("INSERT INTO FL_DM_Sales SELECT * FROM DTL_DW_HOP2_Sales")
    cursor.execute("INSERT INTO FL_DM_Products SELECT * FROM DTL_DW_HOP1_Products")

    conn.commit()
    cursor.close()
    conn.close()
