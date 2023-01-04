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

#заменим все отсутствующие NaN на интерполированные значения столбца Age
df['Age'] = df['Age'].interpolate()


#инфо по датасету
df.info()

#мужчины-женщины на борту
df.groupby('Sex')['PassengerId'].count()

#классы билетов
df.groupby('Pclass')['PassengerId'].count()

#описательная статистика возраста пассажиров
df.Age.describe()

#описательная статистика тарифов билетов
df.Fare.describe()

#братьев и сестер на борту
df.SibSp.unique()
df.SibSp.describe()

#родителей- детей на борту
df.Parch.unique()
df.Parch.describe()
