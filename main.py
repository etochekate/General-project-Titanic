import pandas as pd

df = pd.read_csv('./test.csv')

#print(df.head(10))

#сумма нулевых значений
print(df.isnull().sum())
