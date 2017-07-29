import nltk
import random
from nltk.corpus import brown

#All of the different categories that are tagged in the corpus
print(brown.categories())

#A random sentence from the "humor" category
total = []
sentences = brown.sents(categories = 'humor')
for sentence in sentences:
    sentence = ' '.join(sentence)
    total.append(sentence)
print('\n',random.choice(total))

#The category with the most words
categ_count = {}
count = []

for category in brown.categories():
    words = brown.words(categories = category)
    count.append(len(words))
    categ_count[category] = len(words)
count = sorted(count)

for category in categ_count:
    if categ_count[category] == count[-1]:
        print('\n',category)
