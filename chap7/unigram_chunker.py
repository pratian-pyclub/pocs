import nltk
from nltk.corpus import conll2000

TEST_SENTS = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
TRAIN_SENTS = conll2000.chunked_sents('train.txt', chunk_types=['NP'])

# UnigramChunker takes tag and chunk as inputs
# tag => DT, JJ, NN (represented as t)
# chunk => B-NP, I-NP or O (represented as c)
# word represented as w
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents=TRAIN_SENTS):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def accuracy(test_sents=TEST_SENTS):
        print(self.tagger.evaluate(test_sents))

    def parse(self, sentence):
        sentence = nltk.pos_tag(nltk.word_tokenize(sentence))
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)
