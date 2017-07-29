import nltk
from nltk.corpus import udhr as u
#The full text of the declaration in Ibibio-Efik
print(u.raw('Ibibio_Efik-Latin1'))

#The length (in words) of the text in Amahuaca and in Greenlandic, and which one is longer
word_lenA = len(u.words('Amahuaca'))
word_lenG = len(u.words('Greenlandic_Inuktikut-Latin1'))
print('\nAmahuaca one has %s words and Greenland one has %s words.' % (word_lenA, word_lenG))
if word_lenA > word_lenG:
	print('Amahuaca one is longer.')
else:
	print('Greenland one is longer.')

#The first sentence of the text in Turkish
sentences = u.sents('Turkish_Turkce-Turkish')
sentence1 = ' '.join(sentences[1])
print('\n',sentence1)
