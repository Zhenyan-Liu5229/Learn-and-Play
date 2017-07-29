import nltk
from nltk.book import *
movie = text6

#attempt: get ten actual sentences in conversation
parts = ''
for word in movie:
	parts = parts+word+' '
sentences = nltk.tokenize.sent_tokenize(parts)
for sentence in sentences[:10]:
	print(sentence)

#the number of words
print('\nTne total number is %s.\n'%(len(movie)))

#concordance of string 'coconut'
movie.concordance('coconut')

#the words similar to 'knight'
movie.similar('knight')
