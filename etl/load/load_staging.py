from config.db_connection import get_connection
import pandas as pd

# Normalize all date-like columns to YYYY-MM-DD
def normalize_dates(df):
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            ).dt.date
    return df

# Replace NaN / NaT with None (MySQL compatible)
def normalize_nulls(df):
    return df.where(pd.notnull(df), None)

# Load DataFrame into staging table
def load_dataframe(table, df):
    conn = get_connection()
    cursor = conn.cursor()
    df = normalize_dates(df)
    df = normalize_nulls(df)
    table_cols = ",".join(df.columns)
    table_values = ",".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table} ({table_cols}) VALUES ({table_values})"

    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
