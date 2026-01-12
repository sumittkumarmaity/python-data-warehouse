import pandas as pd
from etl.extract.csv_reader import read_csv
from etl.load.load_staging import load_dataframe

def load_sales():
    files = {
        "Sales_Data_2020.csv": 2020,
        "Sales_Data_2021.csv": 2021,
        "Sales_Data_2022.csv": 2022
    }

    frames = []
    for file, year in files.items():
        print(f"Loading Sales Data from files ('{file}') - Year - ('{year}')...")
        df = read_csv(file)
        df["SalesYear"] = year
        frames.append(df)

    final_df = pd.concat(frames)
    load_dataframe("staging_Sales", final_df)
