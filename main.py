import pandas as pd

df = pd.read_csv('./test.csv')

#print(df.head(10))

#сумма нулевых значений
#print(df.isnull().sum())

#первые 10 строк
df.head(10)

#сумма нулевых значений
df.isnull().sum()

#описание числовых колонок
df.describe()

#размер датасета
df.shape

#количество уникальных значений в каждой колонке
df.nunique()
