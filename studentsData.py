
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

# we sorting the level columb in ascending order
df.sort_values(by=['Level'], ascending=True)


# Showing students who match exam  condition for course work based project 
df[df["Students"] < 71]
df.loc[(df['Students'] < 71) & (df['Exam'] ==  0)]

# plots the student data
df.plot.scatter(x = 'Level', y = 'Students')
