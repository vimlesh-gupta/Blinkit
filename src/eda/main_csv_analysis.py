from src.eda.clean_transform import enrich_orders_with_time_features, merge_orders_with_items_and_products
from src.eda.eda import (
    get_most_common_order_time,
    get_average_basket_size,
    get_top_categories_by_units,
    get_seasonal_trends,
    get_reorder_stats,
    get_top_cities_by_orders,
    get_reorder_distribution
)
from src.eda.load_data import load_all_data
from src.eda.visualizations import (
    plot_monthly_sales_trend,
    plot_sales_heatmap,
    plot_top_categories,
    plot_order_time_heatmap,
    plot_basket_size_histogram,
    plot_reorder_pie
)

# Load and preprocess
orders, order_items, customers, products, customer_feedback, marketing_performance = load_all_data()
orders = enrich_orders_with_time_features(orders)
orders_full = merge_orders_with_items_and_products(orders, order_items, products)

# 1. Most common order time
day, hour, combo = get_most_common_order_time(orders)
print("Most Common Order Day:", day)
print("Most Common Order Hour:", hour)
print("Top Day-Hour Combos:\n", combo)


# 2. Average basket size
basket_size = get_average_basket_size(order_items)
print(f"Average basket size: {basket_size:.2f} items per order")

# 3. Top categories
top_categories = get_top_categories_by_units(products, order_items)
print("Top Categories by Units Sold:\n", top_categories)

# 4. Reorder rate
reorders, rate = get_reorder_stats(orders, customers)
print(f"Customers with >1 order: {reorders}")
print(f"Reorder Rate: {rate:.2f}%")

# 5. Top cities
top_cities = get_top_cities_by_orders(orders, customers)
print("Top Cities by Order Count:\n", top_cities)

# 6. Sales trend visuals
monthly_sales, pivot_table = get_seasonal_trends(orders_full)
plot_monthly_sales_trend(monthly_sales)
plot_sales_heatmap(pivot_table)

# 7. Top categories bar chart
plot_top_categories(top_categories)

# 8. Heatmap of order volume by Day of Week and Hour
plot_order_time_heatmap(orders)

# 9. Histogram of basket sizes (items per order)
plot_basket_size_histogram(order_items)

# 10. Pie chart of reorder vs one-time customers
# Get reorder data
reorder_counts, reorder_labels = get_reorder_distribution(orders, customers)

# Plot pie chart
plot_reorder_pie(reorder_counts, reorder_labels)
