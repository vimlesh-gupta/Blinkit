import pandas as pd
from sqlalchemy import text


def run_query(engine, query):
    """
    Executes a SQL query using the provided SQLAlchemy engine and returns the result as a DataFrame.

    Parameters:
        engine: SQLAlchemy engine connected to your database.
        query: A raw SQL query string.

    Returns:
        A pandas DataFrame containing the result of the query.
    """
    try:
        # Use SQLAlchemy's text() to safely execute the query
        return pd.read_sql(text(query), con=engine)
    except Exception as e:
        # Print the error and return an empty DataFrame if something goes wrong
        print("❌ Error executing SQL query:")
        print(e)
        return pd.DataFrame()
