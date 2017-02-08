import nltk
from nltk.corpus import conll2000
TRAIN_SET = conll2000.chunked_sents('train.txt', chunk_types=['NP'])

def npchunk_features(sentence, i, history):
    word, pos = sentence[i]

    return {"pos": pos}

# def npchunk_features(sentence, i, history):
#     word, pos = sentence[i]
#     if i == 0:
#         prevword, prevpos = "<START>", "<START>"
#     else:
#         prevword, prevpos = sentence[i-1]
#
#     return {"pos": pos, "prevpos": prevpos}

# def npchunk_features(sentence, i, history):
#     word, pos = sentence[i]
#     if i == 0:
#         prevword, prevpos = "<START>", "<START>"
#     else:
#         prevword, prevpos = sentence[i-1]
#
#     return {"pos": pos, "word": word, "prevpos": prevpos}

# def npchunk_features(sentence, i, history):
#     word, pos = sentence[i]
#     if i == 0:
#         prevword, prevpos = "<START>", "<START>"
#     else:
#         prevword, prevpos = sentence[i-1]
#
#     if i == len(sentence)-1:
#         nextword, nextpos = "<END>", "<END>"
#     else:
#         nextword, nextpos = sentence[i+1]
#
#     return {
#                 "pos": pos,
#                 "word": word,
#                 "prevpos": prevpos,
#                 "nextpos": nextpos,
#                 "prevpos+pos": "%s+%s" % (prevpos, pos),
#                 "pos+nextpos": "%s+%s" % (pos, nextpos),
#                 "tags-since-dt": tags_since_dt(sentence, i)
#             }

def tags_since_dt(sentence, i):
    tags = set()
    for word, pos in sentence[:i]:
        if pos == 'DT':
            tags = set()
        else:
            tags.add(pos)

    return '+'.join(sorted(tags))

class ConsecutiveNPChunkTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                print featureset
                print tag
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.MaxentClassifier.train(
            train_set, algorithm='megam', trace=0)
        # self.classifier = nltk.MaxentClassifier.train(
        #     train_set, algorithm="iis")

    def tag(self, sentence):
        history = []
        sentence = nltk.pos_tag(nltk.word_tokenize(sentence))
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(self, train_sents=TRAIN_SET):
        tagged_sents = [[((w,t),c) for (w,t,c) in
                         nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    # this is the activate function
    # pass in a string sentence to extract the noun phrase chunks
    def parse(self, sentence):
        sentence = nltk.pos_tag(nltk.word_tokenize(sentence))
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)
