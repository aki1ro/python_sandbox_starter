import pandas as pd
import numpy as np

pd.options.display.max_columns = 6

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

array = df[['Pclass', 'Fare', 'Age']].values # <---- .values is used to convert to a numpy array This is also considered a 2-dimensional domain
print(array[0, 1]) # <--- this selects the first row and the second column
print(array[:,2]) # <--- used for selecting an entire column
print(array[0]) # < --- used for selecing a single row

mask = array[:,2] > 18 #If true then adult (>18) if false then child (<18)

array[mask]
print(array[mask])
print(array[array[:,2] > 18])

print(mask.sum())
print((array[:,2] > 18).sum()) # <--- returns back the sum of 1's and 0' interpereted as True and False
print(df.head())
print(df.describe()) #Returns a table of statistics about the columns in the dataframe.

print(np.median(df['Age'])) #selects a single column which is known as a Panda Series

small_df = df[['Age', 'Sex', 'Survived']] #<---- this is a creating a dataframe, use double brackets to select multiple columns
series = df['Age'] # <---- this is a series, use a single bracket to select single column
print(small_df.head()) # <---- Prints first 5 rows
print(series)

df['Expensive(if over $32)'] = df['Fare'] > 32

print(df.head(10))

print(df['Age'].values) # <--- This is considered a 1-dimensional array

print(array.shape) # <---- returns the number of rows and columns in a given numpy array

print(df.shape) # <--- returns number of rows and columns for dataframes too

print("value here:")






