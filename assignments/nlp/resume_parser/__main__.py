import nltk
from nltk.tag import StanfordNERTagger
import codecs
from conf import *

class Extractor:
	def __init__(self,text):
		# Converting the input texts into lower-case
		self.text = text
		self.company = self.extract_using_ne()
		if len(self.company) == 0:
			# self.text = text.lower()
			self.extract_full_info()
			self.company = self.extract_company()


	def extract_using_ne(self):
		ner = StanfordNERTagger(CLASSIFIER_PATH, JAR_PATH) 
		tagged_words = ner.tag(nltk.word_tokenize(self.text))
		company = []
		for word, pos in tagged_words:
			if(pos == 'ORGANIZATION'):
				company.append(word)
		return company


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
		with codecs.open(LOC_PATH, 'r', 'utf-8') as file:
			locations = file.read()
			for location in locations.split('\n'):
				parse_tree[location] = 'COMPANY'

		tagger = nltk.tag.UnigramTagger(model=parse_tree)
		for information in self.chunked_words:
			result = tagger.tag(nltk.word_tokenize(information))

		company.extend([word for (word, pos) in result if pos == 'COMPANY'])
		return company


text = "AI Developer at Skcript."
ex = Extractor(text)
print ex.company