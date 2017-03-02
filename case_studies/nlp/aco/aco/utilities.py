# -*- coding: utf-8 -*-
from collections import defaultdict
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

# stemming words
def stem_words(words):
    return [stemmer.stem(word) for word in words]

# clean up string by removing punctuation, lowercasing, and stemming
def normalize(text):
    return stem_words(nltk.word_tokenize(text.lower().translate(depunctuation_map)))

# Using the SnowballStemmer
stemmer = nltk.stem.snowball.SnowballStemmer('english')
# using a term frequency–inverse document frequency
vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
# storing ASCII values of punctuation marks
depunctuation_map = dict((ord(char), None) for char in string.punctuation)

# get cosine similarity
def simscore(text1, text2, showmatch=False):
    vt = vectorizer.fit_transform([text1, text2])
    return ((vt * vt.T).A)[0,1]

def get_top_simscores(simscores, max_top=0):
    ordered = sorted(simscores)[::-1]
    if max_top != 0:
        return ordered[0:max_top]
    else:
        return ordered

def get_init_combi(defaultValue=0):
    return defaultdict(lambda: defaultValue, {})

def flatten(simscores, combi):
    for score in simscores:
        combi[score.values()[0]['member_id']] += score.keys()[0]

    return combi

def beautify_and_sort(combi):
    arc = map(lambda com: {combi[com]: com}, combi)
    return get_top_simscores(arc)

# from nltk.corpus import stopwords
# english = set(stopwords.words('english'))
# def simscore(text_1, text_2, showmatch=False):
#     s = SequenceMatcher(lambda x: x in english, text_1, text_2)
#     if showmatch:
#         print s.find_longest_match(0, 5, 0, 9)
#         print "-"
#         print s.get_matching_blocks()
#         print "--=--"
#     return s.ratio()
