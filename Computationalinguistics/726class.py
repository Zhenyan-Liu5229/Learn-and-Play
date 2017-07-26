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

#recursive grammar
import random
def generate(symbol, output):
    if '*' in symbol:
        rate = random.random()
        if rate > 0.5:
            symbol = symbol[0]
        else:
            symbol = ''

    if symbol.isupper():
        for s in grammar[symbol]:
            generate(s, output)
    else:
        if symbol:
            output.append(symbol)
    return output

grammar = {'S':['A','B'],
            'A':['C','a'],
            'B':['A','b'],
            'C':['A*','c']
            }

output = []
for symbol in grammar['S']:
    generate(symbol,output)
print(output)

#English sentence generation
import random

def generate(sentence, symbol):
    for next_symbol in grammar[symbol]:
        if next_symbol.isupper():
            generate(sentence,next_symbol)
        else:
            s = random.choice(grammar[symbol])
            sentence.append(s)
            return 

grammar = {'S':['NP','VP'],
           'NP':['D','ADJP','N'],
           'D':['a','the'],
           'ADJP':['A'],
           'A':['big','tall','red','gree'],
           'N':['cat','tree','parrot','viking'],
           'VP':['V'],
           'V':['jumps','eats','sings','throws']
           }
sentence = []

generate(sentence,'S')
sentence = '.'.join(sentence)
print(sentence)
