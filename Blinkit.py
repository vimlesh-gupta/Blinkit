import pandas as pd

# 1. What are the most common order times (hours, days)?
df1=pd.read_csv("blinkit_orders.csv")
df1['order_date']=pd.to_datetime(df1['order_date'])
df1['Hour']=df1['order_date'].dt.hour
df1['Minute']=df1['order_date'].dt.minute
df1['Day']=df1['order_date'].dt.day_name()
df1.to_csv("blinkit_orders.csv", index=False)

common_order_day=df1['Day'].value_counts().head(1)
common_order_hour=df1['Hour'].value_counts().head(1)

# print("Most Common Order Day:")
# print(common_order_day)
# print("\nMost Common Order Hour:")
# print(common_order_hour)
#
# most_common_day_and_time_combo=df1.groupby('Day')['Hour'].size().sort_values(ascending=False).reset_index().head(5)
# print("Most Common Day & Time Combination:\n",most_common_day_and_time_combo)


# 2. What is the average basket size (items per order)?
df2=pd.read_csv("blinkit_order_items.csv")
average_basket_size=df2.groupby('order_id')['quantity'].sum().mean()
#print(f"\nAverage basket size: {average_basket_size:.2f} items per order")

# 3. What is the most popular category by total units sold?
df3=pd.read_csv("blinkit_products.csv")
merged_df=pd.merge(df3,df2,on='product_id')

category_by_total_unit=merged_df.groupby('category')['quantity'].sum().reset_index()
print(category_by_total_unit.rename(columns={'quantity':'Total Unit Sold'}))