import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

def get_engine():
    try:
        server=os.getenv(r"SERVER")
        database=os.getenv("DATABASE")
        driver=os.getenv("DRIVER")

        if not all([server,database,driver]):
            raise ValueError("One or more environment variable are missing.")

        connection_string=f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes"
        engine=create_engine(connection_string)

        # Test the connection
        with engine.connect() as conn:
            print("✅ Successfully connected to the database")

        return engine

    except Exception as e:
        print("❌ Error connecting to the database:")
        print(e)
        return None





# This block is used to establish a connection between Pandas and SQL Server using the `pyodbc` library,
# instead of SQLAlchemy.
#
# conn=pyodbc.connect(
#     'DRIVER={SQL Server};'
#     r'Server=LAPTOP-QJ57PKLS\SQLEXPRESS;'
#     'Database=Blinkit;'
#     'Trusted_Connection=yes;'
# )
#
# cursor=conn.cursor()