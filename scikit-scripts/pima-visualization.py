import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

filepath = os.path.abspath(__file__)
PWDPATH = os.path.dirname(filepath)
# df = pd.read_csv('/Users/swaathi/Skcript/Pratian/pocs/scikit-scripts/pima-indian.csv')
df = pd.read_csv(PWDPATH + '/pima-indian.csv')

# Saving Outcome to y Dataframe
# We do not want to normalize on Outcome
y = pd.DataFrame(df['Outcome'], columns=['Outcome'])
df.drop(['Outcome'], axis=1, inplace=True)

# Applying min_max_scaler to 'X'
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled)

df_normalized.rename(columns={
0:'Pregnancies',
1:'Glucose',
2:'BloodPressure',
3:'SkinThickness',
4:'Insulin',
5:'BMI',
6:'DiabetesPedigreeFunction',
7:'Age'}, inplace=True)

# Concatinating normalized 'X' and y
df = pd.concat([df_normalized, y], axis=1)

# Pairplotting
# http://seaborn.pydata.org/generated/seaborn.pairplot.html
sns.pairplot(df, hue="Outcome")
plt.show()
