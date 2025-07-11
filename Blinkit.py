import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. What are the most common order times (hours, days)?
df1=pd.read_csv("blinkit_orders.csv")
df1['order_date']=pd.to_datetime(df1['order_date'])
df1['Hour']=df1['order_date'].dt.hour
df1['Minute']=df1['order_date'].dt.minute
df1['Day']=df1['order_date'].dt.day_name()
df1['Day_Of_Week']=df1['order_date'].dt.dayofweek   # 0=Monday, 6=Sunday
df1['Month']=df1['order_date'].dt.month
df1['Week']=df1['order_date'].dt.isocalendar().week.apply(lambda d: (d - 1) // 7 + 1)
df1['Year']=df1['order_date'].dt.year

#df1.to_csv("blinkit_orders.csv", index=False)

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
# print(category_by_total_unit.rename(columns={'quantity':'Total Unit Sold'}))

# 4. Are there seasonal trends in product sales?
merged_df2=pd.merge(df1,df2,on="order_id")
merged_df3=pd.merge(merged_df2,df3,on='product_id')

yearly_sales=merged_df2.groupby('Year')['quantity'].sum().reset_index()
print("\n",yearly_sales)
monthly_sales=merged_df2.groupby(['Year','Month'])['quantity'].sum().reset_index()
print("\n",monthly_sales)
# Product-specific weekly trend
weekly_sales=merged_df3.groupby(['product_name','Year','Month','Week'])['quantity'].sum().sort_values(ascending=False).reset_index()
print("\n",weekly_sales)

# plotting loop
for y in monthly_sales['Year'].unique():
    data = monthly_sales[monthly_sales['Year'] == y]
    plt.plot(data['Month'], data['quantity'], label=str(y))

# Add labels and legend
plt.title("Monthly Sales Trend by Year")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()

# Pivot your data into a matrix (Month as rows, Year as columns)
pivot_table = merged_df2.pivot_table(index='Month', columns='Year', values='quantity', aggfunc='sum')

# Create the heatmap
plt.figure(figsize=(10,6))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt=".0f")
plt.title("Monthly Sales Heatmap by Year")
plt.show()