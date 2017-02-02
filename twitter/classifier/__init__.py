# -*- coding: utf-8 -*-
import yaml
import nltk
# http://www.nltk.org/howto/collocations.html
# http://www.nltk.org/_modules/nltk/collocations.html
from nltk.collocations import *
from nltk.metrics import BigramAssocMeasures
from sklearn.externals import joblib
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud


from paths import POSPATH, NEGPATH, N_FEATURES, CLASSIFIER_FILE

def load_yaml_files():
    posyml = []
    with open(POSPATH, 'r') as posfile:
        posyml = yaml.load(posfile)

    negyml = []
    with open(NEGPATH, 'r') as negfile:
        negyml = yaml.load(negfile)

    return posyml, negyml

POSYML, NEGYML = load_yaml_files()

class NBClassifier():
    def __init__(self, load=False):
        self.bigram_measures = nltk.collocations.BigramAssocMeasures()
        self.classifier = None
        self.get_all_words()
        self.top_words()
        self.word_cloud()
        self.top_bigrams()

        if load:
            self.load()
        else:
            self.train()

    def get_all_words(self):
        self.all_words = []
        for pos in POSYML:
            self.all_words += [word for word in nltk.word_tokenize(pos['text'])]

        for neg in NEGYML:
            self.all_words += [word for word in nltk.word_tokenize(neg['text'])]

    def top_bigrams(self, n=N_FEATURES):
        finder = BigramCollocationFinder.from_words(self.all_words)
        finder.apply_freq_filter(3)

        # ignoring all bigrams which occur less than n times
        # freq_bigrams = finder.nbest(self.bigram_measures.pmi, n)
        freq_bigrams = finder.nbest(self.bigram_measures.chi_sq, n)

        self.bigram_features = dict([(bigram, True) for bigram in freq_bigrams])

    def accepted_word(self,word):
        accept = True
        if word in stopwords.words('english'):
            accept = False
        elif len(word) < 4 :
            accept = False
        elif isinstance(word, unicode):
            accept = False
        return accept 

    def top_words(self, n=N_FEATURES):
        freq_words = nltk.FreqDist(word for word in self.all_words)
        self.freq_words = nltk.FreqDist(word for word in self.all_words if self.accepted_word(word))
        print self.freq_words.most_common(100)
        # self.word_features = list(self.all_words)[:n]
        freq_words = list(self.all_words)[:n]
        self.word_features = dict([(word, True) for word in freq_words])

    def word_cloud(self):
        wordcloud = WordCloud(width=1000, height=1000).generate_from_frequencies(self.freq_words.most_common(50))
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()
        

    def document_features(self, sentence):
        features = {}

        sentence_words = nltk.word_tokenize(sentence)
        finder = BigramCollocationFinder.from_words(sentence_words)
        # sentence_bigrams = [bigram for (bigram, score) in finder.score_ngrams(self.bigram_measures.pmi)]
        sentence_bigrams = [bigram for (bigram, score) in finder.score_ngrams(self.bigram_measures.chi_sq)]

        for bigram in self.bigram_features:
            features[bigram] = (bigram in sentence_bigrams)

        for word in self.word_features:
            features[word] = (word in sentence_words)

        return features

    def train(self):
        train_set = [(self.document_features(pos['text']), 'pos') for pos in POSYML]
        train_set += [(self.document_features(neg['text']), 'neg') for neg in NEGYML]

        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def save(self):
        # save classifier
        with open(CLASSIFIER_FILE,'wb') as file:
            joblib.dump(self.classifier, file)

    def load(self):
        # load classifier
        with open(CLASSIFIER_FILE, 'rb') as file:
            if file.read(1) != '':
                self.classifier = joblib.load(file)

    def classify(self, sentence):
        return self.classifier.classify(self.document_features(sentence))

    def accuracy(self):
        train_set = [(self.document_features(pos['text']), 'pos') for pos in POSYML]
        train_set += [(self.document_features(neg['text']), 'neg') for neg in NEGYML]

        return nltk.classify.accuracy(self.classifier, train_set)
