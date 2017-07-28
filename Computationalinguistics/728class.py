# List Comprehensions
words = [line.strip() for line in file]
uppercase = [letter.upper() for word in lowercase]
doubles = [n*2 for n in range(10)]

#List filtering
filtered_list = [word for word in word_list
                if len(word) <5
                and word[0].isupper()]
#nltk
from nltk.book import *
text1.concordance('god')
text2.concordance('god')
text3.concordance('god', lines = 10, width = 30)

text1.similar('monstrous')
text2.similar('monstrous')
text3.similar('monstrous')
help(text1.similar)

from nltk.corpus import sinica_treebank
import random

num = random.choice([n for n in range(len(indian.sent()))])
print(indian.sents([num]))

sinica_treebank.parsed_sents()[888].draw()

from nltk.corpus import gutenberg as G
print(G.fileids())
emma = G.words('austen-emma.txt')

#number of words in one txt
for fileid in G.fileids():
    words = G.words(fileid)
    print(fileid, len(words))

#number of letters in one txt
num_chars = len(G.raw('austen-emma.txt'))
print(num_chars)

for fileid in G.fileids():
    num_chars = len(G.raw(fileid))
    num_words = len(G.words(fileid))
    num_sents = len(G.sents(fileid))
    num_vocab = len(set(w.lower() for w in G.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

    #bigram
text = 'a long time ago in a galaxy far far away'.split()
bigrams = {}

for index, word in enumerate(text):
    try:
        try:
            bigrams[word].append(text[index+1])
        except KeyError:
            bigrams[word] = []
            bigrams[word].append(text[index+1])
    except IndexError:
        pass
print(bigrams)
#or
from collections import defaultdict
text = 'a long time ago in a galaxy far far away'.split()
bigrams = defaultdict(list)

def make_grams(n):
    grams = {}
    for index, word in enumerate(text):
        try:
            n = n-1
            grams[word].append(text[index+n])
        except IndexError:
           pass
    return grams

print(make_grams(2))
