from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

def get_topics(self, review):
	raw = review.lower()
	tokens = tokenizer.tokenize(raw)

	print(tokens)