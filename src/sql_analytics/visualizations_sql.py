import matplotlib.pyplot as plt
import seaborn as sns


def plot_delivery_time_vs_rating(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, y="delivery_time_minute", x="rating", alpha=0.5)
    plt.title("Delivery Time vs Customer Rating")
    plt.xlabel("Customer Rating")
    plt.ylabel("Delivery Time (minutes)")
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\scatterplot_of_delivery_time_customer_rating.png',
        dpi=300, bbox_inches='tight')
    plt.show()


def plot_total_revenue_by_category(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="Total_Revenue", y="Product_Category", hue="Product_Category", palette="viridis",
                legend=False)
    plt.title("Total Revenue by Product Category")
    plt.xlabel("Revenue")
    plt.ylabel("Product Category")
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\barplot_of_total_revenue_by_category.png',
        dpi=300, bbox_inches='tight')
    plt.show()


def plot_top_customers(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="Total_Order", y="customer_name", hue="customer_name", palette="coolwarm", legend=False)
    plt.title("Top 5 Customers by Order Value")
    plt.xlabel("Total Order Value")
    plt.ylabel("Customer")
    plt.tight_layout()
    plt.savefig(r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\barplot_of_top_customer.png',
                dpi=300, bbox_inches='tight')
    plt.show()


def plot_conversion_rate(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="conversion_rate_percentage", y="campaign_name", hue="campaign_name", palette="magma",
                legend=False)
    plt.title("Conversion Rate by Campaign")
    plt.xlabel("Conversion Rate (%)")
    plt.ylabel("Campaign")
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\barplot_of_conversion_rate.png',
        dpi=300, bbox_inches='tight')
    plt.show()


def plot_new_customers_monthly(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="Registration_Month", y="New_Customers", marker="o")
    plt.title("New Customers Acquired Each Month")
    plt.xlabel("Month")
    plt.ylabel("New Customers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\line_plot_of_new_customer_every_month.png',
        dpi=300, bbox_inches='tight')
    plt.show()


def plot_monthly_revenue_heatmap(pivot_df):
    """
    Plots heatmap of monthly revenue by city.
    Input must be a pivoted DataFrame (area × month-year).
    """
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot_df, annot=True, fmt=".0f", cmap="YlGnBu", linewidths=.5)
    plt.title("Monthly Revenue per City")
    plt.xlabel("Month")
    plt.ylabel("City")
    plt.xticks(rotation=45)
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\heatmap_of_monthly_revenue_by_city.png',
        dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(corr_matrix):
    """
    Plots a heatmap of correlation matrix.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(
        r'D:\Data Analytics Project\Blinkit_Data_Analytics_Project\outputs\visuals\heatmap_of_correlation_matrix.png',
        dpi=300, bbox_inches='tight')
    plt.show()
