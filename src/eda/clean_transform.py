import pandas as pd


def enrich_orders_with_time_features(orders_df):
    """
    Adds time-based features to the orders dataframe.
    Columns: Hour, Minute, Day, Day_Of_Week, Month, Week, Year
    """
    orders_df = orders_df.copy()
    orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
    orders_df['Hour'] = orders_df['order_date'].dt.hour
    orders_df['Minute'] = orders_df['order_date'].dt.minute
    orders_df['Day'] = orders_df['order_date'].dt.day_name()
    orders_df['Day_Of_Week'] = orders_df['order_date'].dt.dayofweek
    orders_df['Month'] = orders_df['order_date'].dt.month
    orders_df['Week'] = orders_df['Week'] = orders_df['order_date'].dt.isocalendar().week
    orders_df['Year'] = orders_df['order_date'].dt.year
    return orders_df


def merge_orders_with_items_and_products(orders_df, order_items_df, products_df):
    """
    Returns: merged dataframe: orders + order_items + products
    """
    merged = pd.merge(orders_df, order_items_df, on='order_id')
    merged = pd.merge(merged, products_df, on='product_id')
    return merged


def merge_orders_with_customers(orders_df, customers_df):
    """
    Returns: orders enriched with customer info
    """
    return pd.merge(orders_df, customers_df, on='customer_id')


def basic_cleaning(df):
    """
    Apply common cleaning steps like removing nulls, stripping whitespace, etc.
    """
    df = df.dropna(how='all')  # Drop fully empty rows
    df.columns = df.columns.str.strip()
    return df
