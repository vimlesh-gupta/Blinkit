import pyodbc

conn=pyodbc.connect(
    'DRIVER={SQL Server};'
    r'Server=LAPTOP-QJ57PKLS\SQLEXPRESS;'
    'Database=w3school;'
    'Trusted_Connection=yes;'
)

cursor=conn.cursor()

cursor.execute("Select * from employees")

for row in cursor.fetchall():
    print(row)