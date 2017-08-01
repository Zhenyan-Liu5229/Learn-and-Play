#unicode
a = '[\u006D\u00E6\u0283\u026A\u014B]'
print(a)

#decision trees
file = open('D:\\code\\UBC\\language_ID(1).csv')

lines = []

for line in file:
    line = line.strip()
    lines.apppend(line) 
file.close()   
    
data = []
for index.line in enumerate(lines):
    line = line.split(',')
    data.append(({headers[n]:1
                 }))

    #2017.8.1
#machine learning neural network
#word 
import pybrain
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

file = open('D:\\code\\UBC\\1.txt', encoding = 'utf-8-sig')
lines = []
for line in file:
    line = line.strip()
    lines.append(line)
file.close()

imputs = []
outputs = []
for line in lines:
    line = line.split(',')
    code = []
    for letter in line[0]:
        if letter.isupper():
            code.append(1.0)
        else:
            code.append(0.0)
    imputs.append(code)
    outputs.append([float(n) for n in line[1:]])

longest = 0
for i in imputs:
    if len(i) >longest:
        longest - len(i)

dataset = SupervisedDataSet(longest, 3)
network = buildNetwork(longest, 1, 3)
