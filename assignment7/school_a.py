import sqlite3
import pandas as pd


with  sqlite3.connect("../school.db") as conn: 
    print("Database created and connected successfully.")
cursor = conn.cursor()


cursor.execute("""
               CREATE TABLE IF NOT EXISTS Students (student_id INTEGER PRIMARY KEY,
               name TEXT NOT NULL UNIQUE,
               age INTEGER,
               major TEXT)
               """)

cursor.execute("SELECT * FROM Students")
result = cursor.fetchall()
print(result)
for row in result:
    print(row)

