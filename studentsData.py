
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

#plots the data on a bar
df.sort_values(by='Students', ascending=False).plot(kind="bar", rot=0, x = 'Level', y = 'Students')

#Displays data on a bar standing
df2.plot.bar(width=0.9,x='Students',y="Average Grade")

# comparasion the exam and average grades
df2.sort_values(by='Students').plot(kind="barh", x="Exam", y="Average Grade")
