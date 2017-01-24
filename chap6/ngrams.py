import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

print("Unigrams!")
unigram_tagger = nltk.UnigramTagger(train_sents)

print("Tagging #2007")
print(unigram_tagger.tag(brown_sents[2007]))

print("Accuracy is ...", unigram_tagger.evaluate(test_sents))

print("\nBigrams!")
bigram_tagger = nltk.BigramTagger(train_sents)

print("Tagging #4203")
print(bigram_tagger.tag(brown_sents[4203]))

print("Accuracy is ...", bigram_tagger.evaluate(test_sents))

print("\nCombining taggers")
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)

print("Tagging #3682")
print(bigram_tagger.tag(brown_sents[3682]))

print("Accuracy is ...", t2.evaluate(test_sents))
