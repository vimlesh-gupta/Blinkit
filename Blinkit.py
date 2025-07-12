import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

 #1. What are the most common order times (hours, days)?
orders_df=pd.read_csv("blinkit_orders.csv")
orders_df['order_date']=pd.to_datetime(orders_df['order_date'])
orders_df['Hour']=orders_df['order_date'].dt.hour
orders_df['Minute']=orders_df['order_date'].dt.minute
orders_df['Day']=orders_df['order_date'].dt.day_name()
orders_df['Day_Of_Week']=orders_df['order_date'].dt.dayofweek   # 0=Monday, 6=Sunday
orders_df['Month']=orders_df['order_date'].dt.month
orders_df['Week']=orders_df['order_date'].apply(lambda x: (x.day - 1) // 7 + 1)
orders_df['Year']=orders_df['order_date'].dt.year

#orders_df.to_csv("blinkit_orders.csv", index=False)

common_order_day=orders_df['Day'].value_counts().head(1)
common_order_hour=orders_df['Hour'].value_counts().head(1)

print("Most Common Order Day:")
print(common_order_day)
print("\nMost Common Order Hour:")
print(common_order_hour)

most_common_day_and_time_combo=orders_df.groupby('Day')['Hour'].size().sort_values(ascending=False).reset_index().head()
print("\nMost Common Day & Time Combination:\n",most_common_day_and_time_combo)


# 2. What is the average basket size (items per order)?
order_items_df=pd.read_csv("blinkit_order_items.csv")
average_basket_size=order_items_df.groupby('order_id')['quantity'].sum().mean()
print(f"\nAverage basket size: {average_basket_size:.2f} items per order")

# 3. What is the most popular category by total units sold?
products_df=pd.read_csv("blinkit_products.csv")
products_with_order=pd.merge(products_df, order_items_df, on='product_id')

category_by_total_unit=products_with_order.groupby('category')['quantity'].sum().sort_values(ascending=False).reset_index().head()
print("\n",category_by_total_unit.rename(columns={'quantity':'Total Unit Sold'}))

# 4. Are there seasonal trends in product sales?
orders_with_items=pd.merge(orders_df, order_items_df, on="order_id")
orders_with_items_and_products=pd.merge(orders_with_items, products_df, on='product_id')

yearly_sales=orders_with_items.groupby('Year')['quantity'].sum().reset_index()
print("\n",yearly_sales.head())
monthly_sales=orders_with_items.groupby(['Year', 'Month'])['quantity'].sum().reset_index()
print("\n",monthly_sales.head())
# Product-specific weekly trend
weekly_sales=orders_with_items_and_products.groupby(['product_name', 'Year', 'Month', 'Week'])['quantity'].sum().sort_values(ascending=False).reset_index()
print("\n",weekly_sales.head())

# plotting loop
plt.figure(figsize=(10, 5))
for y in monthly_sales['Year'].unique():
    data = monthly_sales[monthly_sales['Year'] == y]
    plt.plot(data['Month'], data['quantity'], marker='o', label=str(y))

# Add labels and legend
plt.title("Monthly Sales Trend by Year")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()

# Pivot your data into a matrix (Month as rows, Year as columns)
pivot_table = orders_with_items.pivot_table(index='Month', columns='Year', values='quantity', aggfunc='sum')

# Create the heatmap
plt.figure(figsize=(10,6))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt=".0f")
plt.title("Monthly Sales Heatmap by Year")
plt.tight_layout()
plt.show()


# 5. How many customers have made more than one order?
customers_df=pd.read_csv("blinkit_customers.csv")
ordered_with_customer=pd.merge(orders_df, customers_df, on="customer_id")

customer_order_count=ordered_with_customer.groupby('customer_id')['order_id'].nunique()
customers_with_multiple_orders=customer_order_count[customer_order_count>1]
customers_with_multiple_orders=customers_with_multiple_orders.count()
print("\nCustomers with more than one order:",customers_with_multiple_orders)

# 6. What is the reorder rate (customers ordering again)?
total_customers=customer_order_count.shape[0] # we can also use count() instead of shape[]
reorder_rate=customers_with_multiple_orders/total_customers*100
print(f"\nReorder Rate: {reorder_rate:.2f}%")

# 7. Which city has the highest order frequency?
highest_order_frequency_by_city=ordered_with_customer.groupby(['area'])['order_id'].nunique().sort_values(ascending=False).head(5)
print("\nTop 5 Cities with Highest Order Counts:\n",highest_order_frequency_by_city)