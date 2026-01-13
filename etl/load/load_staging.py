from config.db_connection import get_connection
import pandas as pd


def normalize_dates(df):
    """
    Normalize all date-like columns to YYYY-MM-DD
    Handles mixed formats safely (new Pandas default behavior)
    """
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            ).dt.date
    return df


def normalize_nulls(df):
    """
    Replace NaN / NaT with None (MySQL compatible)
    """
    return df.where(pd.notnull(df), None)


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
