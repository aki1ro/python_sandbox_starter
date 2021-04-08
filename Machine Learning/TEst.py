import pandas as pd
import numpy as np



df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

array = df[['Pclass', 'Fare', 'Age']].values
 

df['male'] = df['Sex'] == 'male'
df['female'] = df['Sex'] == 'female'
print(df.head())
print("Math:", 5 + 5)
print("Math:", 20/2)

print("Median of All:", np.median(df[['Survived', 'Pclass', 'Age', 'Fare']]))

df['Sex'].values

print(df['Sex'])








