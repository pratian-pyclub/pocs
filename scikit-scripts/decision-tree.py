from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from nltk import word_tokenize, pos_tag
from nltk.corpus import brown
# for pretty printing
from pprint import pprint

# pprint( pos_tag( word_tokenize("That guy helped her to write beautiful poems") ) )
'''
[('That', 'DT'),
 ('guy', 'NN'),
 ('helped', 'VBD'),
 ('her', 'PRP'),
 ('to', 'TO'),
 ('write', 'VB'),
 ('beautiful', 'JJ'),
 ('poems', 'NNS')]
'''
TRAIN_SPLIT = 1
# tagged_sentences= pos_tag(brown.sents()[0])
tagged_sentences = [[
(u'This', u'AT'), (u'Fulton', u'NP-TL'), (u'County', u'NN-TL'), (u'Naveen', u'NN'), (u'Jury', u'NN-TL'), (u'said', u'NN'),
(u'Friday', u'NR'), (u'an', u'AT'), (u'investigation', u'NN'), (u'of', u'IN'), (u"Atlanta's", u'NP$'), (u'recent', u'JJ')
]]


def features(sentence, index):
    """ sentence: [w1, w2, ...], index: the index of the word """
    return {
        'word': sentence[index],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'prev_word': '' if index == 0 else sentence[index - 1],
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }

training_sentences = tagged_sentences[:int(TRAIN_SPLIT*len(tagged_sentences))]
testing_sentences = tagged_sentences[int(TRAIN_SPLIT*len(tagged_sentences)):]

def untag(tagged_sentence):
    return [w for w, t in tagged_sentence]

def to_dataset(tagged_sentences):
	x,y = [],[]
	for tagged in tagged_sentences:
		for index in range(len(tagged)):
			x.append(features(untag(tagged),index))
			y.append(tagged[index][1])
	return x,y


feature, predict = to_dataset(training_sentences[:])


classfier = Pipeline([
    ('vectorizer', DictVectorizer(sparse=False)),
    ('classifier', DecisionTreeClassifier(criterion='entropy'))
])

# Use only the first 10K samples if you're running it multiple times. It takes a fair bit :)
classfier.fit(feature[:], predict[:])

def pos_tag(sentence):
    tagged_sentence = []
    tags = classfier.predict([features(sentence, index) for index in range(len(sentence))])
    return zip(sentence, tags)

# Because of our trained tagger says 'said' as NOUN
print pos_tag(word_tokenize('This is said friend, John.'))
