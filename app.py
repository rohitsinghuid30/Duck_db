import duckdb
import time
import pandas as pd


import sqlite3

conn = sqlite3.connect("src/db/mydb.db")

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS person (id INT, name TEXT, dept TEXT);")
cursor.execute("INSERT INTO person VALUES (1, 'rohit', 'IT');")

conn.commit()

cursor.close()

conn.close()


