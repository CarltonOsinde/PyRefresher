#Pandas

import pandas as pd

#Adding data to your Pandas data structure

#NOTE: You have to use ([[ values, values]], columns=["name","name"])
data = pd.DataFrame([[1,2,3],[4, 5, 6],[7,8,9]])
print(data)

#Adding column names

#NOTE: Column names have to match the columns of data
data = pd.DataFrame([[1,2,3],[4, 5, 6],[7,8,9]],columns=["Price","Age","Value"])

print(data)


