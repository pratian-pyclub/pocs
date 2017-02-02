# -*- coding: utf-8 -*-
import yaml
import nltk
import re
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from pandas import *
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from random import shuffle
from paths import POSPATH, NEGPATH, N_FEATURES, CLASSIFIER_FILE

def load_yaml_files():
    posyml = []
    with open(POSPATH, 'r') as posfile:
        posyml = yaml.load(posfile)

    negyml = []
    with open(NEGPATH, 'r') as negfile:
        negyml = yaml.load(negfile)

    return posyml, negyml

def set_features(sentence):
	return{
		'text' : sentence,
		'contains_animal' : bool(re.search('animal.|cruel*', sentence, re.IGNORECASE)),
		'contains_bull' : bool(re.search('save [a-zA-Z]* bull', sentence, re.IGNORECASE)),
		'contains_torment' : bool(re.search('torment|tortur*', sentence, re.IGNORECASE)),
		'contains_save' :  bool(re.search('save', sentence, re.IGNORECASE)),
		'contains_yoddha' : bool(re.search('yoddhas?', sentence, re.IGNORECASE)),
		'contains_disgrace': bool(re.search('disgrace', sentence, re.IGNORECASE)),
		'contains_brain' : bool(re.search('brain*', sentence, re.IGNORECASE)),
		'contains_profanity' : bool(re.search('barbar*|ruthless',sentence, re.IGNORECASE)),
		'contains_midnight' : bool(re.search('mid[/-]*night?',sentence, re.IGNORECASE))

		#'bigrams' : [b for l in sentence for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]

	}

POSYML, NEGYML = load_yaml_files()

X,Y = [],[]

for i in range(len(POSYML)):
	X.append(set_features(POSYML[i]['text']))
	Y.append(POSYML[i]['sent'])

for i in range(len(NEGYML)):
	X.append(set_features(NEGYML[i]['text']))
	Y.append(NEGYML[i]['sent'])

indexes = [i for i in range(len(X))]
shuffle(indexes)
x,y=[],[]
for i in range(len(X)):
	x.append(X[i])
	y.append(Y[i])


classifier = Pipeline([
    ('vectorizer', DictVectorizer(sparse=False)),
    ('classifier', SVC())
])

classifier.fit(x[1000:2000],y[1000:2000])

print classifier.score(x[:1000],y[:1000])


# print classifier.predict(set_features('animal cruelty is bad'))
