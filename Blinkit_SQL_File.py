import pandas as pd
import pyodbc
import sqlite3
from sqlalchemy import create_engine,text
import glob

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
total_revenue_per_product_category_query= """select p.category as Product_Category,Sum(oi.quantity * oi.unit_price) as Total_Revenue
from Blinkit.dbo.blinkit_order_items oi
join Blinkit.dbo.blinkit_products p on oi.product_id=p.product_id
group by p.category
order by Total_Revenue desc"""

revenue_by_product_category=pd.read_sql_query(text(total_revenue_per_product_category_query), con=engine)
#print("Total Revenue By Product Category:\n",revenue_by_product_category)

# 2.Who are the top 10 customers by total order value?
top_10_customer_by_total_order_query= """ select top 10 c.customer_id,c.customer_name,sum(o.order_total) as Total_Order
from Blinkit.dbo.blinkit_orders o
join Blinkit.dbo.blinkit_customers c on o.customer_id=c.customer_id
group by c.customer_id,c.customer_name
order by Total_Order desc """

top_10_customer_by_total_order=pd.read_sql_query(text(top_10_customer_by_total_order_query),engine)
#print(f"\nTop 10 Customer by Total Order Value:\n",top_10_customer_by_total_order)

# 3. What is the average number of items per order?
Average_Item_Per_Order_query=""" select 
sum(quantity) / count(distinct order_id) 
As Average_Item_Per_Order 
from Blinkit.dbo.blinkit_order_items """

Average_Item_Per_Order=pd.read_sql_query(text(Average_Item_Per_Order_query),engine)
#print(Average_Item_Per_Order)

# 4. Which product has the highest total sales?
products_by_highest_total_sale_query="""select Top 10 p.product_name, sum(oi.quantity) as Total_Sold_Quantity
from Blinkit.dbo.blinkit_products p
join Blinkit.dbo.blinkit_order_items oi on p.product_id=oi.product_id
group by p.product_name
order by Total_Sold_Quantity desc"""

products_by_highest_total_sale=pd.read_sql_query(text(products_by_highest_total_sale_query),engine)
#print("\n",products_by_highest_total_sale)

# 5. What is the conversion rate for each marketing campaign?
conversion_rate_percentage_query=""" select campaign_name,sum(conversions) *100.0 / NULLIF(SUM(clicks), 0) as conversion_rate_percentage from Blinkit.dbo.blinkit_marketing_performance
group by campaign_name
order by conversion_rate_percentage desc """

conversion_rate_percentage=pd.read_sql_query(conversion_rate_percentage_query,engine)
#print("\n",conversion_rate_percentage)

#6. How many new customers joined each month?
new_customers_each_month_query=""" select format(registration_date, 'yyyy-MM') as Registration_Month, count(customer_id) as New_Customers
from Blinkit.dbo.blinkit_customers
group by format(registration_date, 'yyyy-MM')
order by Registration_Month """

new_customers_each_month=pd.read_sql_query(text(new_customers_each_month_query),engine)
print("\n",new_customers_each_month)