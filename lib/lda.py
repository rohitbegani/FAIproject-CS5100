from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

import numpy as np
import lda

tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

def get_topics(review):
	raw = review.lower()
	tokens = tokenizer.tokenize(raw)
	stopped_tokens = [i for i in tokens if not i in en_stop]
	texts = [p_stemmer.stem(i) for i in stopped_tokens]
	model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
	model.fit(texts)
	print model

