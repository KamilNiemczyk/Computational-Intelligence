# import pandas as pd
# df = pd.read_csv("iris.csv")
# # print(df)
# # print(df.values)

# #wszystkie wiersze, kolumna nr 0
# # print(df.values[:, 0])
# a=df.values[:, 0]
# b=[1.0, 2.0, 3.0, 4.0]
# print(type(a))
# print(type(b))
# #wiersze od 5 do 10, wszystkie kolumny
# # print(df.values[5:11, :])
# # #dane w komórce [1,4]
# # print(df.values[1, 4])


import pandas as pd

missing_values = ["n/a", "na", "-", "--", 0]   #symbole które będą interpretowane jako błędna linia
# df = pd.read_csv("iris_with_errors.csv")
df = pd.read_csv("iris_with_errors.csv", na_values= missing_values)  #zamienia symbopl z missing values na "na"
print(df.isnull().sum())
# print(df.isnull())
types= df.dtypes
print(types)




