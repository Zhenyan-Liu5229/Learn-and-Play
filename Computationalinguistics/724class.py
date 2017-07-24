#2017.7.24
#Type casting
dozen = 12
print(dozen, type(dozen))
dozen = str(dozen)  #from integer to string
print(dozen, type(dozen)) 

place = 'Vancouver'
print(list(place))
place = '200'
print(int(place))
vowels = ['e','a','o']
print(str(vowels))
print(''.join(vowels))

#loop-stoping
random_words=['pumpkin','shark','idea','level','oval']
vowels = ['a','o','e','i','u']

for word in random_words:
    if word[0] in vowels: #try not in vowels (print 'pumpkin)
        print(word)
        break
else:
    print('Yeah')
print('Aha')\

#enumerate
long_word = 'asdfertd'
for index, letter in enumerate(long_word):
    print(index,letter)

#sorted
for vowel in sorted(vowels):
    print(vowel)
vowels.sort()
print(vowels)

#practice Chaha
labial = ['p','b','f','v','m']
dorsal = ['k','g','x','q']
words = []
file = open('D:\\code\\1.txt')
for line in file:
    line = line.strip()
    line = line.split(',')
    line = line[0]
    words.append(line)
file.close()
    
for word in words:
    word = list(word)
    word.reverse()
    for i, letter in enumerate(word):
        if letter in labial or letter in dorsal:
            index = i
            break
    else:
        index = 999

    if index != 999:
        word.insert(index,'w')
    word.reverse()
    word = ''.join(word) 
    print(word)          

#practice on Saisiyat nouns
file = open('D:\\code\\1.txt',)
words = []
for line in file:
    line = line.strip()   
    if not line:
        continue
    line = line.split(',')
    words.append(line[0])
file.close()

reduplicants = []
suffix = 'an'
for word in words:
    reduplicant = word[:3]+word+'an'
    reduplicants.append(reduplicant)
for n in range(len(words)):
    print(words[n],reduplicants[n])
