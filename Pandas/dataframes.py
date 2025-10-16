import pandas as pd

a = [1, 2, 3, 4, 5]
s = pd.DataFrame(a)
print(s)

data = {
    'Name': ['Shravani', 'Kiran', 'Sandhya', 'Shravya'],
    'Age': [20, 25, 22, 5]
}
df = pd.DataFrame(data)
print(df)

print("Age column:\n", df['Age'])
