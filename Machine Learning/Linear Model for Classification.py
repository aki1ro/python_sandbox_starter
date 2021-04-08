import numpy as np
import pandas as pd
import matplotlib

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

array = df[['Fare', 'Age']].values

print(array[0])
print(df.shape)
print(array[array[:,1] > 60])

