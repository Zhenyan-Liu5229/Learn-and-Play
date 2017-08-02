#2017.8.2
#list comprehension
letters = ['a','b','c','d']
uppers = [letter.upper() for letter in letters]
print(uppers)

#dictionary comprehesions
numbers = [1,2,3,4,5]
doubles = {n:n*2 for n in numbers}

upper_s = {letter:letter.upper() for letter in letters}
print(upper_s)

#numbers = [1 if letter == 'T' else 0 for letter in letters]

#classifier
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

def load_training_data(path):
    file = open(path)
    file.readline()
    lines = [line.strip() for line in file]
    file.close()
    inputs = []
    outputs = []
    for line in lines:
        line = line.split(',')
        inputs.append([float(n) for n in line[1:5]])
        outputs.append([float(n) for n in line[5:]])
    return inputs, outputs

inputs,outputs = load_training_data('D:\\code\\UBC\\classifier.csv')

#Create a dataset from pybrain
dataset = SupervisedDataSet(4, 5)
for index in range(len(inputs)):
    dataset.addSample(tuple(inputs[index]), tuple(outputs[index]))

#Build a network that uses backpropogration
network = buildNetwork(4, 6, 5)
trainer = BackpropTrainer(network, dataset)

#Train the network with 20 examples of each training item
for j in range(100):
    trainer.train()

#Test the network
#test_words = [[0,1,0,0]]
for index, input_ in enumerate(inputs):
    results  = network.activate(input_)
    print(results)
    highest = max(results)
    if highest == results[0]:
        category = 'zuo'
    elif highest == results[1]:
        category = 'qun'
    elif highest == results[2]:
        category = 'zhang'
    elif highest == results[3]:
        category = 'tiao' 
    else:
        category = 'ke'
    print ('is probably a', category)
