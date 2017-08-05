from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

#open file and get Mongolian words
file = open('D:\\code\\UBC\\mon.txt', encoding = 'utf-8')
lines = []
for line in file:
    line = line.strip()
    line = line.strip('\ufeff')
    line = line.split('\t')
    lines.append(line[0])
file.close()

#input nodes with original length
input_raw = []
for word in lines:
    word_parts = word.split('.')
    code = []
    for syllable in word_parts:
        syllable = syllable.strip('\'')
        for i,letter in enumerate(syllable):
            try:
                if letter == syllable[i+1]:
                    code.append(1.0)
                    break
            except IndexError:
                pass 
        else:
            code.append(0.0)         
    input_raw.append(code)

#final inputs nodes with the same length
inputs = []
for code in input_raw:
    while len(code) < 5: # 5 is the max(len(raw_input in in input_raw))
        code.append(-1.0)
    inputs.append(code)

#outputs
outputs=[]
for i, word in enumerate(lines):
    if 1.0 not in inputs[i]:
        node = [1.0, 0.0]
    else:
        node = [0.0, 1.0]
    outputs.append(node)

#Create a file of original words and its presentations
file = open('D:\\code\\UBC\\assignment3.txt', mode = 'w', encoding = 'utf-8')
for n in range(len(lines)):
    line = lines[n]+' '+str(inputs[n])+' '+str(outputs[n]) +'\n'
    file.write(line)
file.close()


#Create a dataset from pybrain
dataset = SupervisedDataSet(5, 2)
for index in range(len(inputs)):
    dataset.addSample(tuple(inputs[index]), tuple(outputs[index]))

#Build a network that uses backpropogration
network = buildNetwork(5, 5, 2)
trainer = BackpropTrainer(network, dataset)

#Train the network with 100 examples of each training item
for j in range(100):
    trainer.train()

for index, input_ in enumerate(inputs):
    results  = network.activate(input_)
    print(results)
    highest = max(results)
    if highest == results[0]:
        category = 'stress the first syllable' 
    else:
        category = 'stress the right-most long vowel'
    print ('It probably needs to', category)
