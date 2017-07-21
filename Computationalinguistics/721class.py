#2017.7.21
#loop the number
for number in range (0,13):
    print(number)

#practice fizzbuzz
print(15%4)
for number in range (1,101):
    if number %3 == 0:
        if number %5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    elif number %5 == 0:
        print('buzz')
    else:
        print(number)

#file 2
#strip the affix
line='apple/'
print(line.strip('/'))

#practice language data
file = open('D:\\code\\1.txt')
locations = {}
family = {}
sound = {}
for line in file:
    line = line.strip()
    #some need line = line.strip('\ufeff')
    line = line.split(':')
    if line[0] == 'Language':
        language = line[1]
    elif line[0] == 'Family':
        family[language] = line[1]
    elif line[0] == 'Location':
        locations[language] = line[1]
    elif line[0] == 'Inventory':
        inventory = line[1].split(',')
        sound[language] = inventory 

for language in locations:
    if locations[language] in ['Canada','USA']:
        print(language,'is native to NA.')
for language in family:
    if family[language] == 'Indo-European':
        print(language,'belongs to Indo-European.')
for language in sound:
    if 's' in sound[language]:
        print(language,'has the /s/ sound.')

#practice Cherokee
file = open('D:\\code\\1.txt',encoding='utf-8')
file.readline()
for line in file:
    line = line.strip()
    line = line.split(',')
    gloss = line[2].split(' ')
    if 'tree' in gloss:
        print(line[0],line[2])
file.close()

#file writing 
path = 'D:\\code\\class.txt'
file = open(path, mode = 'a') #'w'mode will not save the file
file.write('new line one')
file.close()

tables = {1:['Xue,Yuyan'],
          2:[],
          3:['Leon','Justin','Bowen','Cathy','Shamy','Victor'],
          4:['James','Anita','Jeff']
          }

base = 'D:\\code\\'

for number in range(1,5):
    filename = 'table'+ str(number)+'.txt'
    path = base+filename
    file = open(path, mode = 'w', encoding = 'utf-8')
    for person in tables[number]:
        file.write(person+'\n')
file.close()

file = open('D:\\code\\1.txt')
words = []
for line in file:
    line = line.strip()
    line = line.split(',')
    words.append(line[0])

for word in words:
    reduplication = word[0]+'a'+word
    print(word,reduplication)
#another
reduplications = []
    #reduplications.append(reduplication)
#for n in range(len(words)):
    #print(word[n],reduplication[n])
