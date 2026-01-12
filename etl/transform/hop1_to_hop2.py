from config.db_connection import get_connection

def Load_DTL_DW_HOP_2():
    conn = get_connection()
    cursor = conn.cursor()
    print(f"Loading Data from DTL_DW_HOP1_Customers to DTL_DW_HOP2_Customers ...")
    cursor.execute("""
        INSERT INTO DTL_DW_HOP2_Customers
        SELECT * FROM DTL_DW_HOP1_Customers
    """)
    print(f"Loading Data from DTL_DW_HOP1_Sales to DTL_DW_HOP2_Sales ...")
    cursor.execute("""
        INSERT INTO DTL_DW_HOP2_Sales
        SELECT * FROM DTL_DW_HOP1_Sales
    """)

    conn.commit()
    cursor.close()
    conn.close()
