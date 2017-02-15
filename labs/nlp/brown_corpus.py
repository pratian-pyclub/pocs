from nltk.corpus import brown

tagged_words = brown.tagged_words(categories="news")
# which nouns are more common in plural form than singular?
# NNS - plural, NN - singular. Calculate plural = singular + s

s_nouns = [w for (w,t) in tagged_words if t == "NN"]
plurals = set([w + "s" for w in s_nouns])
p_nouns = [w for (w,t) in tagged_words if t == "NNS" and w in plurals]
s_fd = nltk.FreqDist(s_nouns)
p_fd = nltk.FreqDist(p_nouns)

print "words where singular > plural=", \
  filter(lambda word: s_fd[word] < p_fd[word], p_fd.keys())[:50]

# which word has the greatest number of distinct tags
word_tags = nltk.defaultdict(lambda: set())
for word, token in tagged_words:
  word_tags[word].add(token)

ambig_words = sorted([(k, len(v)) for (k, v) in word_tags.items()],
  key=itemgetter(1), reverse=True)[:50]
print [(word, numtoks, word_tags[word]) for (word, numtoks) in ambig_words]

# list top 20 (by frequency) tags
token_fd = nltk.FreqDist([token for (word, token) in tagged_words])
print "top_tokens=", token_fd.keys()[:20]

# which tags are nouns most commonly found after
tagged_word_bigrams = nltk.bigrams(tagged_words)
fd_an = nltk.FreqDist([t1 for (w1,t1),(w2,t2)
  in tagged_word_bigrams if t2.startswith("NN")])

print "nouns commonly found after these tags:", fd_an.keys()
