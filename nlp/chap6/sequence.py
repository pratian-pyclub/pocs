import nltk
from nltk.corpus import brown

def pos_features(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
                 "suffix(2)": sentence[i][-2:],
                 "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):
    def __init__(self, train_sents=brown.tagged_sents(categories='news')):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set.append((featureset, tag))
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

# tagged_sents = brown.tagged_sents(categories='news')
# size = int(len(tagged_sents) * 0.1)
# train_sents, test_sents = tagged_sents[size:], tagged_sents[:size]
# tagger = ConsecutivePosTagger(train_sents)
# print(tagger.evaluate(test_sents))

# tagger.tag(brown.sents(categories='news')[0])
