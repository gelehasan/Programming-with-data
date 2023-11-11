
import pandas as pd
# import csv

df = pd.read_csv("sample.csv")


df["Students"].describe()

df.tail(3)
# slicing to explore at more depth.
df[6:9]

df["Students"].mean()

df["Students"].describe()

df.shape

# replacing the index numbers with the courses code
df.set_index("Code", inplace=True)

# identifying some trends at a cursory level.
df.sort_values(by=['Level'], ascending=True)
