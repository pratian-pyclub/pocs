import pandas as pd
import numpy as np

# Scikit-learn is the most popular Python machine learning framework and for good reason
from sklearn.utils import shuffle
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier


names = pd.read_csv('names_dataset.csv')
# as_matrix converts into matrix form
# the index is used to eliminate the first id column.
names = names.as_matrix()[:,1:]


TRAIN_SPLIT = 0.75

def features(name):
	name = name.lower()
	return {
		'first-letter': name[0],
		'first-2letter': name[:2],
		'first-3letter': name[:3],
		'last-3letter': name[-3:],
		'last-2letter': name[-2:],
		'last-letter': name[-1]
	}

# Vectorizing the function to accept the array/list of names i.e, strings
features = np.vectorize(features)

# print features(['naveen','anish'])
# The output for the above statement will be as follows:
# [
#		{'first-2letter': 'na', 'last-letter': 'n', 'first-letter': 'n', 'last-3letter': 'een', 'last-2letter': 'en', 'first-3letter': 'nav'}
#  	{'first-2letter': 'an', 'last-letter': 'h', 'first-letter': 'a', 'last-3letter': 'ish', 'last-2letter': 'sh', 'first-3letter': 'ani'}
# ]

xfeature = features(names[:,0]) # We need only the name column
gender = names[:,1]
xfeature, gender = shuffle(xfeature, gender)

feature_train, feature_test = xfeature[:int(TRAIN_SPLIT * len(xfeature))], xfeature[int(TRAIN_SPLIT * len(xfeature)):]
gender_train, gender_test = gender[:int(TRAIN_SPLIT * len(gender))], gender[int(TRAIN_SPLIT * len(gender)):]

# Transforms lists of feature-value mappings to vectors.
# This transformer turns lists of mappings (dict-like objects) of feature names to feature values into Numpy arrays or scipy.sparse matrices for use with scikit-learn estimators.
vectorizer = DictVectorizer()
vectorizer.fit(feature_train)

classifier = DecisionTreeClassifier()
print "Here we are going to train the features with the predictions. It will take some time"
classifier.fit(vectorizer.transform(feature_train),gender_train)

print classifier.predict(vectorizer.transform(features(["Alex", "Emma"])))
print str(classifier.score(vectorizer.transform(feature_train),gender_train)*100)+'%'
