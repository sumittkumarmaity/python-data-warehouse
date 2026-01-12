import pandas as pd
import os

SOURCE_PATH = "source_data"

def read_csv(file_name):
    file_path = os.path.join(SOURCE_PATH, file_name)

    for enc in ["utf-8", "latin1", "cp1252"]:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except UnicodeDecodeError:
            continue

    raise ValueError(f"Unable to read CSV due to encoding issue: {file_name}")

