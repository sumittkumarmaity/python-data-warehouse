from config.db_connection import get_connection

def Load_DTL_DW_HOP_1():
    conn = get_connection()
    cursor = conn.cursor()

    tables = [
        ("staging_Customers", "DTL_DW_HOP1_Customers"),
        ("staging_Products", "DTL_DW_HOP1_Products"),
        ("staging_Territory", "DTL_DW_HOP1_Territory"),
        ("staging_Sales", "DTL_DW_HOP1_Sales")
    ]

    for src, tgt in tables:
        print(f"Loading Data from  ('{src}') to ('{tgt}')...")
        cursor.execute(f"INSERT INTO {tgt} SELECT * FROM {src}")

    conn.commit()
    cursor.close()
    conn.close()
