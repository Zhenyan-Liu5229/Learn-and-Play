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
