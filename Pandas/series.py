import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Pandas Series:\n",series)
print("First element:", series[0])

a = [1, 2, 3, 4, 5]
s = pd.Series(a,index=['a','b','c','d','e'])
print(s)
