import pandas as pd
import pyodbc
import sqlite3
from sqlalchemy import create_engine, text, false
import glob
import matplotlib.pyplot as plt
import seaborn as sns

# This block is used to establish a connection between Pandas and SQL Server using the `pyodbc` library,
# instead of SQLAlchemy.
#
# conn=pyodbc.connect(
#     'DRIVER={SQL Server};'
#     r'Server=LAPTOP-QJ57PKLS\SQLEXPRESS;'
#     'Database=w3school;'
#     'Trusted_Connection=yes;'
# )
#
# cursor=conn.cursor()

driver='SQL Server'
server=r'LAPTOP-QJ57PKLS\SQLEXPRESS'
database='master'

# Create SQLAlchemy engine
connection_string = f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes"
engine = create_engine(connection_string)

#  Create New Database
# new_db_name= 'Blinkit'
# with engine.connect() as conn:
#     conn.execute(text(f"create database {new_db_name}"))
#     print(f"New Database {new_db_name} created successfully.")

# This glob will return a list of all .csv files inside the data/ directory. we use it instead of listdir().
# csv_files=glob.glob("*.csv")
# print(csv_files)

# 1.What is the total revenue per product category?
total_revenue_per_product_category_query= """
select 
p.category as Product_Category,
Sum(oi.quantity * oi.unit_price) as Total_Revenue
from Blinkit.dbo.blinkit_order_items oi
join Blinkit.dbo.blinkit_products p on oi.product_id=p.product_id
group by p.category
order by Total_Revenue desc
"""

df_revenue_by_product_category=pd.read_sql_query(text(total_revenue_per_product_category_query), con=engine)
#print("Total Revenue By Product Category:\n",df_revenue_by_product_category)

# 2.Who are the top 10 customers by total order value?
top_10_customer_by_total_order_query= """ 
select top 10 
c.customer_id,
c.customer_name,
sum(o.order_total) as Total_Order
from Blinkit.dbo.blinkit_orders o
join Blinkit.dbo.blinkit_customers c on o.customer_id=c.customer_id
group by c.customer_id,c.customer_name
order by Total_Order desc """

df_top_10_customer_by_total_order=pd.read_sql_query(text(top_10_customer_by_total_order_query),engine)
#print(f"\nTop 10 Customer by Total Order Value:\n",df_top_10_customer_by_total_order)

# 3. What is the average number of items per order?
Average_Item_Per_Order_query=""" 
select 
sum(quantity) / count(distinct order_id) As Average_Item_Per_Order 
from Blinkit.dbo.blinkit_order_items """

df_Average_Item_Per_Order=pd.read_sql_query(text(Average_Item_Per_Order_query),engine)
#print(df_Average_Item_Per_Order)

# 4. Which product has the highest total sales?
products_by_highest_total_sale_query="""
select Top 10 
p.product_name, 
sum(oi.quantity) as Total_Sold_Quantity
from Blinkit.dbo.blinkit_products p
join Blinkit.dbo.blinkit_order_items oi on p.product_id=oi.product_id
group by p.product_name
order by Total_Sold_Quantity desc"""

df_products_by_highest_total_sale=pd.read_sql_query(text(products_by_highest_total_sale_query),engine)
#print("\n",df_products_by_highest_total_sale)

# 5. What is the conversion rate for each marketing campaign?
conversion_rate_percentage_query=""" 
select 
campaign_name,
sum(conversions) *100.0 / NULLIF(SUM(clicks), 0) as conversion_rate_percentage 
from Blinkit.dbo.blinkit_marketing_performance
group by campaign_name
order by conversion_rate_percentage desc """

df_conversion_rate_percentage=pd.read_sql_query(conversion_rate_percentage_query,engine)
#print("\n",df_conversion_rate_percentage)

#6. How many new customers joined each month?
new_customers_each_month_query=""" 
select 
format(registration_date, 'yyyy-MM') as Registration_Month, 
count(customer_id) as New_Customers
from Blinkit.dbo.blinkit_customers
group by format(registration_date, 'yyyy-MM')
order by Registration_Month 
"""

df_new_customers_each_month=pd.read_sql_query(text(new_customers_each_month_query),engine)
#print("\n",df_new_customers_each_month)

# 7. What is the monthly revenue growth?

# 8. Monthly revenue per product in a specific city
monthly_revenue_per_product_citywise_query=""" 
select  top 10
p.product_name,
o.year,
o.month,
o.month_name,
c.area,
sum(o.order_total) as Monthly_Revenue

from Blinkit.dbo.blinkit_orders o

join Blinkit.dbo.blinkit_customers c on o.customer_id=c.customer_id
join Blinkit.dbo.blinkit_order_items oi on o.order_id=oi.order_id
join Blinkit.dbo.blinkit_products p on oi.product_id=p.product_id

group by p.product_name,c.area,o.year,o.month,o.month_name
order by o.year,o.month
"""

df_monthly_revenue_per_product_citywise=pd.read_sql_query(text(monthly_revenue_per_product_citywise_query),engine)
#print(df_monthly_revenue_per_product_citywise)

# 9. Find the Correlation between order volume and product price.
correlation_between_order_volume_and_price_query="""
select 
p.product_name,
p.price,
sum(oi.quantity) as total_quantity_sold
from Blinkit.dbo.blinkit_order_items oi
join Blinkit.dbo.blinkit_products p on oi.product_id=p.product_id
group by p.product_name,p.price,oi.quantity
order by total_quantity_sold desc
"""
df=pd.read_sql_query(text(correlation_between_order_volume_and_price_query),engine)
#print(df)
correlation=df['price'].corr(df['total_quantity_sold'])
#print(f"Correlation between product price and order volume: {correlation:.2f}")

# 10. Find the Time to delivery and impact on customer satisfaction.
correlation_between_time_to_delivery_and_impact_customer_satisfaction_query="""
select 
o.order_id,
DATEDIFF(MINUTE, o.promised_delivery_time, o.actual_delivery_time) as delivery_time_minute,
f.sentiment
from Blinkit.dbo.blinkit_orders o
join Blinkit.dbo.blinkit_customer_feedback f on o.order_id=f.order_id
where 
f.feedback_category='delivery' and f.sentiment is not null and o.actual_delivery_time is not null
order by delivery_time_minute
"""
df=pd.read_sql_query(text(correlation_between_time_to_delivery_and_impact_customer_satisfaction_query),engine)

# converted sentiment column to numeric value
sentiment_map={"Positive":1, "Neutral":0, "Negative":-1}
df['sentiment_num']=df['sentiment'].map(sentiment_map)

correlation=df['delivery_time_minute'].corr(df['sentiment_num'])
print(f"\n Correlation:{correlation:.2f}")

# Plot: Delivery Time (min) vs Customer Satisfaction: Sentiment
plt.figure(figsize=(10,6))
sns.boxplot(data=df,y="delivery_time_minute",x='sentiment', palette="Set2")
plt.title('Delivery Time vs Customer Sentiment')
plt.xlabel('Customer Sentiment')
plt.ylabel('Delivery Time (minutes)')
plt.tight_layout()
plt.show()