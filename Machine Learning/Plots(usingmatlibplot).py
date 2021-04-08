import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')


plt.scatter(df['Age'], df['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')

plt.scatter(df['Age'], df['Fare'], c = df['Pclass'])

plt.plot([0, 80], [85, 5])

plt.plot([80, 0], [0, 500])

plt.plot([10, 100], [0, 3])

