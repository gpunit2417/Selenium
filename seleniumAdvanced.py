import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Desktop\\data.csv")

# print entire file data
# print(df)

# print specific columns
# data = df[["Name", "Age"]]
# print(data)

# print data at specific row
# data1 = df.loc[2]
# data1 = df.iloc[2]
# print(data1)


# prints data at specific row and column
# data2 = df.at[2, "Name"]
# print(data2)

# data3 = df.iat[2, 1]
# print(data3)