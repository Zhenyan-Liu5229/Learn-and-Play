#language generation
import random
grammar = {'B':['s','v','o',],
           's':['birds','cars','wolves',],
           'v':['eat','like','chase'],
           'o':['cheese','apple','homework']}
sentence = []

for base_symbol in grammar['B']:
    word = random.choice(grammar[base_symbol])
    sentence.append(word)
sentence = ' '.join(sentence)
print(sentence)
