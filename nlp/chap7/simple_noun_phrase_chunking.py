import nltk
# Noun Phrases are sentence phrases that clearly describe a noun
# "the little yellow dog" is a noun phrase, where "dog" is the noun

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)

print(result)

# The result is a tree structure
# You can visualize the tree structure by doing,
result.draw()

# Here's another phrase, this one is called CHUNK
# Notice the previous one was called NP
# These labels are completely customizable

cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
brown = nltk.corpus.brown
for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    # This is how you traverse the chunk tree
    for subtree in tree.subtrees():
            if subtree.label() == 'CHUNK': print(subtree)

# chunks can be of tree or tag (called IOB format) type
# this converts tags to trees traversal
# nltk.chunk.conlltags2tree(conlltags)

# IOB Format (IMAGE: http://www.nltk.org/images/chunk-tagrep.png)
# As befits their intermediate status between tagging and parsing (8.), chunk
# structures can be represented using either tags or trees. The most widespread
# file representation uses IOB tags. In this scheme, each token is tagged with
# one of three special chunk tags, I (inside), O (outside), or B (begin).
# A token is tagged as B if it marks the beginning of a chunk.
# Subsequent tokens within the chunk are tagged I. All other tokens are tagged O.
# The B and I tags are suffixed with the chunk type, e.g. B-NP, I-NP.
# Of course, it is not necessary to specify a chunk type for tokens that appear
# outside a chunk, so these are just labeled O. An example of this scheme is shown in 2.5.
