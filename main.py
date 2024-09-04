import time
import os
import pandas as pd


base_dir = "src/data"
filename = "mydata.csv"
filename2 = "mydata2.csv"

file_path1 = os.path.join(base_dir, filename)
file_path2 = os.path.join(base_dir, filename2)

df = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
# df = pd.read_csv("src/data/mydata.csv")
print(df)
print("")
print(df2)

start_time = time.time()
print(start_time)
print("Hello World")
end_time = time.time()
print(end_time)

time_diff = end_time - start_time
print(time_diff)

print("Hello dear")
