file = open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\hungarian.txt',encoding = 'utf-8-sig')
words = []
for line in file:
    line = line.strip()
    line = line.split('\t')
    words.append(line[1])
file.close()

file = open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\vowels.txt',encoding = 'utf-8-sig')
vowels = []
for line in file:
    line = line.strip()
    line = line.split(',')
    line = line[1:]
    vowels.append(line)
front_vowels = vowels[0]
back_vowels = vowels[1]
neutral_vowels = vowels[2]
file.close()

file = open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\suffixes.txt',encoding = 'utf-8-sig')
back_suffix = []
other_suffix = []
for line in file:
    line = line.strip()
    line = line.split(',')
    back_suffix.append(line[1])
    other_suffix.append(line[2])
file.close()

present_words=[]
future_words=[]
for word in words:
    for letter in word:
        if letter in back_vowels:
            state ='back'
            break
    else:
        state = 'front'
    if state =='back':
        present_words.append(word+back_suffix[0])
        future_words.append(word+back_suffix[1])
    else:  
        present_words.append(word+other_suffix[0])
        future_words.append(word+other_suffix[1])

file = open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\present.txt', mode = 'w', encoding = 'utf-8')
for n in range(len(words)):
    line = words[n]+','+present_words[n]+'\n'
    file.write(line)

file = open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\future.txt', mode = 'w', encoding = 'utf-8')
for n in range(len(words)):
    line = words[n]+','+future_words[n]+'\n'
    file.write(line)
