import matplotlib.pyplot as plt
import seaborn as sns


def plot_monthly_sales_trend(monthly_sales):
    """
    Line plot of monthly sales by year
    Expects columns: ['Year', 'Month', 'quantity']
    """
    plt.figure(figsize=(10, 5))
    for year in monthly_sales['Year'].unique():
        data = monthly_sales[monthly_sales['Year'] == year]
        plt.plot(data['Month'], data['quantity'], marker='o', label=str(year))

    plt.title("Monthly Sales Trend by Year")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.xticks(ticks=range(1, 13), labels=[
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ])
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\line_plot_of_monthly_sales_trend_by_year.png',
        dpi=300, bbox_inches='tight')
    plt.show()


def plot_sales_heatmap(pivot_table):
    """
    Heatmap of sales volume by Month and Year
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap='YlGnBu', linewidths=0.5, linecolor='white')
    plt.title("Monthly Sales Heatmap by Year")
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\heatmap_of_sales_volume_by_month_and_year.png',
        dpi=300, bbox_inches='tight')
    plt.show()


def plot_top_categories(df_top_categories):
    """
    Bar chart for top categories by units sold
    Expects columns: ['category', 'quantity']
    """
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df_top_categories, x='quantity', y='category', hue='category', dodge=False, palette='viridis',
                legend=False)
    plt.title("Top Product Categories by Units Sold")
    plt.xlabel("Total Units Sold")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\bar_chart_for_top_categories_by_units_sold.png',
        dpi=300, bbox_inches='tight')
    plt.show()


# Order Time Analysis (Heatmap of Hour vs Day)
def plot_order_time_heatmap(df):
    """
    Heatmap of order volume by Day of Week and Hour
    Requires 'Day_Of_Week' and 'Hour' columns in df
    """
    heatmap_data = df.pivot_table(index='Day_Of_Week', columns='Hour', values='order_id', aggfunc='count')
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='g')
    plt.title("Order Volume by Hour and Day of Week")
    plt.xlabel("Hour of Day")
    plt.ylabel("Day of Week (0=Mon)")
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\heatmap_of_order_volume_by_day_of_eek_and_hour.png',
        dpi=300, bbox_inches='tight')
    plt.show()


def plot_basket_size_histogram(order_items_df):
    """
    Histogram of basket sizes (items per order)
    """
    basket_sizes = order_items_df.groupby('order_id')['quantity'].sum()
    plt.figure(figsize=(10, 6))
    sns.histplot(basket_sizes, bins=30, kde=True, color='skyblue')
    plt.title("Distribution of Basket Sizes")
    plt.xlabel("Total Items per Order")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\histogram_of_basket_sizes.png',
        dpi=300, bbox_inches='tight')
    plt.show()


def plot_reorder_pie(reorder_counts, labels):
    """
    Pie chart of customer reorder data
    """
    plt.figure(figsize=(6, 6))
    plt.pie(reorder_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#4caf50', '#ff9800'])
    plt.title("Customer Reorder Rate")
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\pie_chart_of_customer_reorder_data.png',
        dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.show()
