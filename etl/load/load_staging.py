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

    # 🔹 Normalize data BEFORE insert
    df = normalize_dates(df)
    df = normalize_nulls(df)

    cols = ",".join(df.columns)
    placeholders = ",".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"

    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
