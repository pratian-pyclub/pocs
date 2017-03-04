import os

import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split

filepath = os.path.abspath(__file__)
PWDPATH = os.path.dirname(filepath)
# CSVPATH = "/Users/swaathi/Skcript/Pratian/pocs/diabetes.csv"
CSVPATH = PWDPATH + '/diabetes.csv'

def read_csv():
    df = pd.read_csv(CSVPATH)

    y = pd.DataFrame(df['Outcome'], columns=['Outcome'])
    df.drop(['Outcome'], axis=1, inplace=True)

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

    return df_normalized, y

def train(train_x, train_y):
    gnb = GaussianNB()
    return gnb.fit(train_x, train_y)

def accuracy(gnb, test_x, test_y):
    pred_y = gnb.predict(test_x)
    # print(metrics.classification_report(pred_y, test_y))
    print accuracy_score(test_y, pred_y)

X, y = read_csv()
train_x, test_x, train_y, test_y = train_test_split(X, y, random_state=0)
gnb = train(train_x, train_y)
accuracy(gnb, test_x, test_y)
