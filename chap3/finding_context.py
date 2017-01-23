import nltk
text = nltk.Text(nltk.corpus.brown.words())

print "Using regex \n \n"
text.findall(r"<.*><.*><.*><.*><.*><.*><hello><.*><.*><.*><.*><.*><.*>")

print "\n\n\n\n\n"

print "Using builtin function \n \n"
text.concordance("hello")
