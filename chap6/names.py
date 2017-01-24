import nltk
from nltk.corpus import names
import random

# returns last letter
# gender_features('shrek')
# >>> {'last_letter': 'k'}
# def gender_features(word):
#     return {'last_letter': word[-1]}

# returns a better feature set
# returns first_letter, last_letter, count and presence indication of letter
def gender_features(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print("Neo is ... ", classifier.classify(gender_features('Neo')))
print("Trinity is ... ", classifier.classify(gender_features('Trinity')))

print("Accuracy is ...", nltk.classify.accuracy(classifier, test_set))

classifier.show_most_informative_features(5)
