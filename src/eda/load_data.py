import glob
import os

import pandas as pd

# Define the base directory for data
data_path = r"D:\Data Analytics Project\Blinkit_Data_Analytics_Project\data\*.csv"


def load_csv_files():
    csv_files = glob.glob(data_path)
    dataframes = {}

    for file in csv_files:
        file_name = os.path.basename(file).replace(".csv", "").replace("blinkit_", "")
        df = pd.read_csv(file)
        dataframes[file_name] = df

    return dataframes


def load_all_data():
    """
       Returns:
           orders_df, order_items_df, customers_df, products_df, customer_feedback_df, marketing_performance_df
       """
    dfs = load_csv_files()
    return (
        dfs.get("orders"),
        dfs.get("order_items"),
        dfs.get("customers"),
        dfs.get("products"),
        dfs.get("customer_feedback"),
        dfs.get("marketing_performance")
    )
