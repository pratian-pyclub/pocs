import nltk
import codecs

class Extractor:
	def __init__(self,text):
		# Converting the input texts into lower-case
		self.text = text.lower()

	# This function
	def extract_full_info(self):
		tagged_sentence = nltk.pos_tag(nltk.word_tokenize(self.text), 'universal')
		grammar = "PLACE: {<NOUN>+<ADP><NOUN>+}"
		parser = nltk.RegexpParser(grammar)
		result = parser.parse(tagged_sentence)

		self.chunked_words = []
		for elem in result.subtrees():
			if elem.label() == 'PLACE':
				self.chunked_words.append(' '.join(word for (word,pos) in elem.leaves()))

		return self.chunked_words

	def extract_company(self):
		company = []
		parse_tree = {}
		with codecs.open('location.txt', 'r', 'utf-8') as file:
			locations = file.read()
			for location in locations.split('\n'):
				parse_tree[location] = 'COMPANY'

		tagger = nltk.tag.UnigramTagger(model=parse_tree)
		for information in self.chunked_words:
			result = tagger.tag(nltk.word_tokenize(information))

		company.extend([word for (word, pos) in result if pos == 'COMPANY'])
		return company

text = "AI Developer at Skcript. Blah blah blah here there"

ex = Extractor(text)
print ex.extract_full_info() # ['developer at skcript']
print ex.extract_company() # ['skcript']
