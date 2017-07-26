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

def generate(symbol, output):
    if symbol.isupper():
        for s in grammar[symbol]:
            generate(s, output)
    else:
        output.append(symbol)
    return output

grammar = {'S':['A','B'],
            'A':['C','a'],
            'B':['A','b'],
            'C':['c']
            }

output = []
for symbol in grammar['S']:
    generate(symbol,output)
print(output)
