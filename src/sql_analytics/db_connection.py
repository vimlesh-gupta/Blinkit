import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from a .env file
load_dotenv()


def get_engine():
    """
    Establishes a SQLAlchemy engine connection to the SQL Server database.
    Requires SERVER, DATABASE, and DRIVER environment variables.

    Returns:
        engine (sqlalchemy.engine.base.Engine) or None if connection fails.
    """
    try:
        server = os.getenv(r"SERVER")
        database = os.getenv("DATABASE")
        driver = os.getenv("DRIVER")

        # Ensure required variables are present
        if not all([server, database, driver]):
            raise ValueError("❌ One or more required environment variables (SERVER, DATABASE, DRIVER) are missing.")

        # Construct SQLAlchemy connection string
        connection_string = f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes"
        engine = create_engine(connection_string)

        # Test the connection
        with engine.connect() as conn:
            print("✅ Successfully connected to the database.")

        return engine

    except Exception as e:
        print("❌ Failed to connect to the database.")
        print(f"Error: {e}")
        return None


# Optional legacy method using pyodbc directly (for reference)
"""
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    r'SERVER=LAPTOP-QJ57PKLS\SQLEXPRESS;'
    'DATABASE=Blinkit;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
"""
