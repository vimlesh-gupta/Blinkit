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
query="""select p.category as Product_Category,Sum(oi.quantity * oi.unit_price) as Total_Revenue
from Blinkit.dbo.blinkit_order_items oi
join Blinkit.dbo.blinkit_products p on oi.product_id=p.product_id
group by p.category
order by Total_Revenue desc"""

revenue_by_product_category=pd.read_sql_query(text(query),con=engine)
print(f"Total Revenue By Product Category:\n{revenue_by_product_category}")