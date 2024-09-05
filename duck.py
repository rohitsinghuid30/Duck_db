import pandas as pd
import duckdb

'''
# query 1
data = duckdb.read_csv("src/data/mydata.csv")
print(data)


print("")
print(f"data2 result is below")
# query 2
data2 = duckdb.sql('SELECT * from "src/data/mydata2.csv";')
print(data2)


print("")
print(f"data3 result with where clause is below")
# query 3
data3 = duckdb.sql('SELECT * from "src/data/mydata2.csv" WHERE age>30')
print(data3)



conn = duckdb.connect("src/db/mydb.ddb")

print("")
# read sql person
data_sql = duckdb.sql('SELECT * FROM person')
print(data_sql.fetchone())
'''

# pandas dataframe
df = pd.read_csv("src/data/mydata2.csv")
data4 = duckdb.sql("select * from df where age>30")
# print(df)
print(data4)


