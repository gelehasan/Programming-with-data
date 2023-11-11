
import pandas as pd
# import csv

df = pd.read_csv("sample.csv")


df["Students"].describe()

df.tail(3)
# You might want to pick some arbitrary slices to explore at more depth.
df[6:9]

df["Students"].mean()

df["Students"].describe()

df.shape
