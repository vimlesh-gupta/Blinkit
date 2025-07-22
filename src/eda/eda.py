import pandas as pd

from src.eda.load_data import load_all_data

orders_df, order_items_df, customers_df, products_df, customers_feedback_df, marketing_performance_df = load_all_data()


def get_most_common_order_time(orders_df):
    """
    Returns: most common day, hour, and day-hour combination
    """
    common_day = orders_df['Day'].value_counts().idxmax()
    common_hour = orders_df['Hour'].value_counts().idxmax()
    combo = orders_df.groupby('Day')['Hour'].size().sort_values(ascending=False).reset_index().head()

    return common_day, common_hour, combo


def get_average_basket_size(order_items_df):
    """
    Returns: average number of items per order
    """
    return order_items_df.groupby('order_id')['quantity'].sum().mean()


def get_top_categories_by_units(products_df, order_items_df, top_n=5):
    """
    Returns: top N product categories by quantity sold
    """
    merged = pd.merge(products_df, order_items_df, on='product_id')
    return merged.groupby('category')['quantity'].sum().sort_values(ascending=False).head(top_n).reset_index()


def get_seasonal_trends(merged_df):
    """
    Returns: monthly sales (for line plot) and pivot table (for heatmap)
    """
    monthly_sales = merged_df.groupby(['Year', 'Month'])['quantity'].sum().reset_index()
    pivot_table = merged_df.pivot_table(index='Month', columns='Year', values='quantity', aggfunc='sum')
    return monthly_sales, pivot_table


def get_reorder_stats(orders_df, customers_df):
    """
    Returns:
    - number of customers with >1 order
    - reorder rate %
    """
    merged = pd.merge(orders_df, customers_df, on='customer_id')
    order_counts = merged.groupby('customer_id')['order_id'].nunique()
    customers_with_reorders = order_counts[order_counts > 1].count()
    total_customers = order_counts.shape[0]
    reorder_rate = (customers_with_reorders / total_customers) * 100
    return customers_with_reorders, reorder_rate


def get_top_cities_by_orders(orders_df, customers_df, top_n=5):
    """
    Returns: top N cities/areas by unique order count
    """
    merged = pd.merge(orders_df, customers_df, on='customer_id')
    return merged.groupby('area')['order_id'].nunique().sort_values(ascending=False).head(top_n).reset_index()


def get_reorder_distribution(orders_df, customers_df):
    """
    Returns:
    - reorder_counts: list of reordered vs one-time customer counts
    - labels: corresponding labels
    """
    merged = pd.merge(orders_df, customers_df, on='customer_id')
    order_counts = merged.groupby('customer_id')['order_id'].nunique()
    reorder_counts = [(order_counts > 1).sum(), (order_counts == 1).sum()]
    labels = ['Reordered (2+ orders)', 'One-Time (1 order)']
    return reorder_counts, labels
