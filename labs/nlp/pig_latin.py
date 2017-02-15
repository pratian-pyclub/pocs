import nltk
import nltk.data
import re
import inflect

p = inflect.engine()

def makePigLatin(word):
    """ convert one word into pig latin """
    m  = len(word)
    vowels = "a", "e", "i", "o", "u", "y"

    # short words are not converted
    if m < 3 or word == "the":
        return word
    else:
        for i in vowels:
            if word.find(i) < m and word.find(i) != -1:
                m = word.find(i)
        if m==0:
            return word + "way"
        else:
            return word[m:] + word[:m] + "ay"

# open sample input
global sample

with open('sample-long.txt', 'r') as f:
    sample = f.read()

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

for sentence in tagged_sentences:
    for tagged_word in sentence:
        print tagged_word
        # skip "("
        if tagged_word[0] in ["(", ")"]:
            continue
        # replace proper nouns with piglatin; using title case
        if tagged_word[1] == 'NNP':
            sample = re.sub(tagged_word[0]+"(\W)", makePigLatin(tagged_word[0]).lower().title() + "\\1", sample)
        # replace singular nouns with piglatin
        if tagged_word[1] == 'NN':
            # if word is title case, keep using title case
            if tagged_word[0].istitle():
                sample = re.sub(tagged_word[0]+"(\W)", makePigLatin(tagged_word[0]).lower().title() + "\\1", sample)
            else:
                sample = re.sub(tagged_word[0] + "(\W)", makePigLatin(tagged_word[0]) + "\\1", sample)
        # replace plural nouns with pig latin
        if tagged_word[1] == 'NNS':
            singular = p.singular_noun(tagged_word[0]);
            piglatin = p.plural_noun(makePigLatin(singular))
            if tagged_word[0].istitle():
                piglatin = piglatin.lower().title()
            sample = re.sub(tagged_word[0]+"(\W)",piglatin+"\\1",sample)

print sample
# output
# As in wipafropki, greeking uxzints inserting kykdokdo vawv or,
# commonly, Vxiic or Nypoz vawv in ndararonis of visual mohia fgupects
# (such as in graphic and lim rojugs) to check the xioyul of the final
# cifnyuh before the actual vawv is available, or to arserwa xioyul
# ihhyhhjyct by ykutuzoquzw the wozmjaqmoyn of readable vawv.  Vawv
# of this meks is known as "greeked vawv", "pyllu vawv", or "jabberwocky
# vawv".  Sutab uflin is a commonly used uxavqmu, though this is
# derived from Nypoz, not Vxiic.
