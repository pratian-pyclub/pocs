import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import check_output
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import export_graphviz
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import confusion_matrix

filepath = os.path.abspath(__file__)
PWDPATH = os.path.dirname(filepath)

df = pd.read_csv(PWDPATH + '/HR_comma_sep.csv')

# dependent salary values
df['salary'].replace({'low':1,'medium':5,'high':10}, inplace=True)
salary = df['salary']

# independent sales values
dummies = pd.get_dummies(df['sales'], prefix='sales')
df = pd.concat([df, dummies], axis=1)
df.drop(['sales'], axis=1, inplace=True)

X = df.drop(['left'], axis=1)
y = df['left']

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

model = RandomForestClassifier(n_estimators=1000)
model.fit(Xtrain, ytrain)
ypred = model.predict(Xtest)
print(metrics.classification_report(ypred, ytest))

mat = confusion_matrix(ytest, ypred)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label');
plt.show()
