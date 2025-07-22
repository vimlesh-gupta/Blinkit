def calculate_correlation(df, col1, col2):
    # Returns the Pearson correlation between two numeric columns
    return df[col1].corr(df[col2])


def prepare_city_month_revenue_data(df):
    """
    Prepares pivoted data for heatmap from raw monthly revenue DataFrame.
    Returns a pivot table: area × month-year.
    """
    df['Month_Year'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2)

    # Aggregate in case multiple products per city-month
    grouped = df.groupby(['Month_Year', 'area'])['Monthly_Revenue'].sum().reset_index()
    pivot = grouped.pivot(index='area', columns='Month_Year', values='Monthly_Revenue').fillna(0)

    return pivot


def calculate_correlations(df):
    """
    Returns correlation matrix and interpretations.
    """
    numeric_cols = ['delivery_time', 'rating', 'product_price', 'quantity', 'revenue']
    df_numeric = df[numeric_cols]
    corr_matrix = df_numeric.corr()

    interpretations = []
    for col1 in numeric_cols:
        for col2 in numeric_cols:
            if col1 != col2:
                value = corr_matrix.loc[col1, col2]
                abs_val = abs(value)
                strength = (
                    "Strong" if abs_val >= 0.7 else
                    "Moderate" if abs_val >= 0.4 else
                    "Weak"
                )
                direction = "Positive" if value > 0 else "Negative"
                interpretations.append(f"{col1} vs {col2}: {strength} {direction} correlation ({value:.2f})")

    return corr_matrix, interpretations
