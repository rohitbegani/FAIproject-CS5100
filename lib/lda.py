from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
#from gensim import corpora, models
from collections import defaultdict


# tokenizer = RegexpTokenizer(r'\w+')
# en_stop = get_stop_words('en')
# p_stemmer = PorterStemmer()
#
#
# def get_topics(review):
# 	frequency = defaultdict(int)
# 	#print review
# 	raw = review.lower()
# 	tokens = tokenizer.tokenize(raw)
# 	stopped_tokens = [i for i in tokens if not i in en_stop]
# 	for token in stopped_tokens:
# 		frequency[token] += 1
# 	texts = [i for i in tokens if frequency[token] > 1]
# 	dictionary = corpora.Dictionary(texts)
# 	print dictionary

