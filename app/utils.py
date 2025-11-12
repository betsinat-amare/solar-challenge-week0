import pandas as pd
import os

def load_data(countries):
    df_list = []
    for c in countries:
        file_path = f"data/{c.lower()}_clean.csv"
        if os.path.exists(file_path):
            temp = pd.read_csv(file_path)
            temp["Country"] = c
            df_list.append(temp)
    if df_list:
        return pd.concat(df_list, ignore_index=True)
    return pd.DataFrame()

def summary_stats(df, metric):
    return df.groupby("Country")[metric].agg(["mean", "median", "std"]).reset_index()
