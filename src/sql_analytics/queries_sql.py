"""
queries_sql.py

This module contains raw SQL queries for various analytics tasks on the Blinkit dataset.
Each query is stored as a string variable for use with SQLAlchemy or Pandas SQL methods.
"""

q_total_revenue_per_product_category = """
SELECT 
    p.category AS Product_Category,
    SUM(oi.quantity * oi.unit_price) AS Total_Revenue
FROM blinkit_order_items oi
JOIN blinkit_products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY Total_Revenue DESC
"""

q_customer_by_total_order_value = """
SELECT 
    c.customer_id, 
    c.customer_name,
    SUM(o.order_total) AS Total_Order
FROM blinkit_orders o
JOIN blinkit_customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY Total_Order DESC
"""

q_average_items_per_order = """
SELECT 
    SUM(quantity) / COUNT(DISTINCT order_id) AS Average_Item_Per_Order
FROM blinkit_order_items
"""

q_products_by_highest_total_sale = """
SELECT 
    p.product_name,
    SUM(oi.quantity) AS Total_Sold_Quantity
FROM blinkit_products p
JOIN blinkit_order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY Total_Sold_Quantity DESC
"""

q_conversion_rate_percentage = """
SELECT 
    campaign_name,
    SUM(conversions) * 100.0 / NULLIF(SUM(clicks), 0) AS conversion_rate_percentage
FROM blinkit_marketing_performance
GROUP BY campaign_name
ORDER BY conversion_rate_percentage DESC
"""

q_new_customers_each_month = """
SELECT 
    FORMAT(registration_date, 'yyyy-MM') AS Registration_Month,
    COUNT(customer_id) AS New_Customers
FROM blinkit_customers
GROUP BY FORMAT(registration_date, 'yyyy-MM')
ORDER BY Registration_Month
"""

q_monthly_revenue_per_product_citywise = """
SELECT 
    p.product_name,
    o.year,
    o.month,
    o.month_name,
    c.area,
    SUM(o.order_total) AS Monthly_Revenue
FROM blinkit_orders o
JOIN blinkit_customers c ON o.customer_id = c.customer_id
JOIN blinkit_order_items oi ON o.order_id = oi.order_id
JOIN blinkit_products p ON oi.product_id = p.product_id
GROUP BY p.product_name, c.area, o.year, o.month, o.month_name
ORDER BY o.year, o.month
"""

q_correlation_order_volume_price = """
SELECT 
    p.product_name, 
    p.price,
    SUM(oi.quantity) AS total_quantity_sold
FROM blinkit_order_items oi
JOIN blinkit_products p ON oi.product_id = p.product_id
GROUP BY p.product_name, p.price, oi.quantity
ORDER BY total_quantity_sold DESC
"""

q_correlation_delivery_time_rating = """
SELECT 
    o.order_id,
    DATEDIFF(MINUTE, o.promised_delivery_time, o.actual_delivery_time) AS delivery_time_minute,
    f.rating
FROM blinkit_orders o
JOIN blinkit_customer_feedback f ON o.order_id = f.order_id
WHERE f.rating IS NOT NULL 
  AND o.actual_delivery_time IS NOT NULL
ORDER BY delivery_time_minute
"""

q_correlation_ready_data = """
SELECT 
    o.order_id,
    DATEDIFF(MINUTE, o.promised_delivery_time, o.actual_delivery_time) AS delivery_time,
    f.rating,
    p.price AS product_price,
    oi.quantity,
    (oi.unit_price * oi.quantity) AS revenue
FROM blinkit_orders o
JOIN blinkit_customer_feedback f ON o.order_id = f.order_id
JOIN blinkit_order_items oi ON o.order_id = oi.order_id
JOIN blinkit_products p ON oi.product_id = p.product_id
WHERE f.rating IS NOT NULL 
  AND o.promised_delivery_time IS NOT NULL
  AND o.actual_delivery_time IS NOT NULL
"""
