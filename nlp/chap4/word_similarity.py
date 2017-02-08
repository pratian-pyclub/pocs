# path_similarity assigns a score in the range 0–1 based on the shortest path that
# connects the concepts in the hypernym hierarchy (-1 is returned in those cases
# where a path cannot be found)

from __future__ import division
from nltk.corpus import wordnet as wn
import sys

def similarity(w1, w2, sim=wn.path_similarity):
  synsets1 = wn.synsets(w1)
  synsets2 = wn.synsets(w2)
  sim_scores = []
  for synset1 in synsets1:
    for synset2 in synsets2:
      sim_scores.append(sim(synset1, synset2))
  if len(sim_scores) == 0:
    return 0
  else:
    return max(sim_scores)

f = open('/Users/swaathi/Skcript/Pratian/CourseWare/Natural Language Processing/pocs/chap4/data', 'rb')
for line in f:
    (word1, word2) = line.strip().split("\t")
    print word1
    print word2
    print similarity(word1, word2)
    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"

f.close()
