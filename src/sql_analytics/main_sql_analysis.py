import queries_sql as q
from db_connection import get_engine
from eda_sql import calculate_correlation, prepare_city_month_revenue_data, calculate_correlations
from query_runner import run_query
from visualizations_sql import (
    plot_delivery_time_vs_rating,
    plot_total_revenue_by_category,
    plot_top_customers,
    plot_conversion_rate,
    plot_new_customers_monthly,
    plot_monthly_revenue_heatmap,
    plot_correlation_heatmap
)

# Initialize DB connection
engine = get_engine()
if not engine:
    exit()

# 1. Total Revenue per Product Category
df1 = run_query(engine, q.q_total_revenue_per_product_category)
plot_total_revenue_by_category(df1)

# 2. Top Customers by Total Order Value
df2 = run_query(engine, q.q_customer_by_total_order_value).head(5)
plot_top_customers(df2)

# 3. Average Number of Items per Order
df3 = run_query(engine, q.q_average_items_per_order)

# 4. Product with Highest Total Sales
df4 = run_query(engine, q.q_products_by_highest_total_sale).head()

# 5. Conversion Rate per Campaign
df5 = run_query(engine, q.q_conversion_rate_percentage)
plot_conversion_rate(df5)

# 6. New Customers per Month
df6 = run_query(engine, q.q_new_customers_each_month)
plot_new_customers_monthly(df6)

# 8. Monthly Revenue per Product per City
df8 = run_query(engine, q.q_monthly_revenue_per_product_citywise).sort_values(by="Monthly_Revenue",
                                                                              ascending=False).head(10)
pivot_df8 = prepare_city_month_revenue_data(df8)
plot_monthly_revenue_heatmap(pivot_df8)

# 9. Correlation: Order Volume vs Product Price
df9 = run_query(engine, q.q_correlation_order_volume_price)
correlation_1 = calculate_correlation(df9, 'price', 'total_quantity_sold')
print(f"\nCorrelation between price and quantity sold: {correlation_1:.2f}")

# 10. Correlation: Delivery Time vs Customer Rating
df10 = run_query(engine, q.q_correlation_delivery_time_rating)
correlation_2 = calculate_correlation(df10, 'delivery_time_minute', 'rating')
print(f"\nCorrelation between delivery time and rating: {correlation_2:.2f}")

# 11. Visualize Delivery Time vs Rating
plot_delivery_time_vs_rating(df10)

# 12. Correlation Analysis
df_corr = run_query(engine, q.q_correlation_ready_data)

# EDA
corr_matrix, interpretations = calculate_correlations(df_corr)

# Print interpretations
print("\n📊 Correlation Interpretations:")
for line in interpretations:
    print(" -", line)

# Visualization
plot_correlation_heatmap(corr_matrix)
