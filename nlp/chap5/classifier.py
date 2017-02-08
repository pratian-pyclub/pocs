import nltk
from collections import Counter

for sent in nltk.corpus.brown.sents()[0:10]:
    pos_count = {}
    pos_count['NNP'] = 0
    pos_count = Counter(pos[1] for pos in nltk.pos_tag(sent))
    if pos_count['NNP'] > 2:
        print " ".join(sent)
        print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"

# You can also create your own grammar taggers using Regex
# patterns = [(r'.*ing$', 'VBG')]
# regexp_tagger = nltk.RegexpTagger(patterns)
# regexp_tagger.tag(nltk.word_tokenize("this is so amazing"))

# If Regex is not enough for your case, you can also provide a dictionary of words
