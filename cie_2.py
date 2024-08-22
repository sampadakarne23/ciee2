# -*- coding: utf-8 -*-
"""cie 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z9uJG3wVb4RAS3UFiQeWKJMNSwvkKo0t
"""

import pandas as pd
import seaborn as sns
data=pd.read_csv('/content/titanic.csv')
df=pd.DataFrame(data)
print(df)

data.head(5)

data.describe()

data.info()

data.isnull().sum()

import numpy as np
from scipy import stats
mean=np.mean(data['Age'])
median=np.median(data['Age'])
mode=stats.mode(data['Age'],keepdims=True).mode[0]
mean1=np.mean(data['Fare'])
median1=np.median(data['Fare'])
mode1=stats.mode(data['Fare'],keepdims=True).mode[0]
print("centeral tendency:")
print("mean:",mean)
print("median:",median)
print("mode:",mode)
print("mean1:",mean1)
print("median1:",median1)
print("mode1:",mode1)

import matplotlib.pyplot as plt
data['Survived'] = df['Survived'].map({1: 'Survived', 0: 'Not Survived'})
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Survived', hue='Pclass', palette='viridis')
plt.title('Survival Count by Passenger Class')
plt.xlabel('Survival Status')
plt.ylabel('Number of Passengers')
plt.legend(title='Pclass')
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
titanic = sns.load_dataset('titanic')
age= titanic['age'].dropna()
z_sc = np.abs(stats.zscore(age))
threshold = 3
outliers_z_score = age[z_sc > threshold]
print("Outliers detected using Z-score method:")
print(outliers_z_score)
plt.figure(figsize=(5,5))
sns.boxplot(y=titanic['age'])
plt.title('Boxplot of Age')
plt.show()

df=data.isnull().sum()
print(df)
t_data=data.fillna(data.mean(numeric_only=True))
print(t_data)