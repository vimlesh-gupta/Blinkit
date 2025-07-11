import pandas as pd


# 2. What is the average basket size (items per order)?
df=pd.read_csv("blinkit_order_items.csv")
average_basket_size=df.groupby('order_id')['quantity'].sum().mean()
print(f"Average basket size: {average_basket_size:.2f} items per order")