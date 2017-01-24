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
def get_score(s1, s2):
    s1 = normalize(s1)
    s2 = normalize(s2)
    vt = vectorizer.fit_transform([s1, s2])
    return ((vt * vt.T).A)[0,1]

for s1 in nltk.sent_tokenize(TEXT):
   for s2 in nltk.sent_tokenize(TEXT):
     if s1 == s2:
      continue
     print(get_score(s1, s2))
     print s2
     print "==\n"
