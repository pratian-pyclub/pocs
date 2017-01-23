import nltk, string
# from nltk.corpus import stopwords
# lowercase, depunc, stopwords

# Using the SnowballStemmer
stemmer = nltk.stem.snowball.SnowballStemmer('english')

# storing ASCII values of punctuation marks
depunctuation_map = dict((ord(char), None) for char in string.punctuation)

# stemming words
def stem_words(words):
    return [stemmer.stem(word) for word in words]

# clean up string by removing punctuation, lowercasing, and stemming
def normalize(text):
    return stem_words(nltk.word_tokenize(text.lower().translate(depunctuation_map)))

text = ""
for sent in nltk.corpus.brown.sents()[0:10]:
    sent = " ".join(sent)
    text += " " + sent

print "Denormalizaed text: \n\n"
print text

print "\n\n\n\n\n"

print "Normalized text: \n\n"
print normalize(text)
