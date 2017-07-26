def file_open(path,n,l,separator):
    file = open(path,encoding = 'utf-8')
    for line in file:
        line = line.strip()
        line = line.split(separator)
        if n in ['words','back_suffix']:
            l.append(line[1])
        elif n == 'vowels':
            l.append(line[1:])
        else:
            l.append(line[2])
    file.close()

def file_write(path,list_name):
    file = open(path, mode = 'w', encoding = 'utf-8')
    for n in range(len(words)):
        line = words[n]+','+list_name[n]+'\n'

words = []
vowels = []
back_suffix = []
other_suffix = []

file_open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\hungarian.txt','words',words,'\t')
file_open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\vowels.txt','vowels',vowels,',')
file_open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\suffixes.txt','back_suffix',back_suffix,',')
file_open('C:\\Users\\Shirley Heather\\Desktop\\UBC\\suffixes.txt','other_suffix',other_suffix,',')

back_vowels = vowels[1]

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

file_write('C:\\Users\\Shirley Heather\\Desktop\\UBC\\present.txt', present_words)
file_write('C:\\Users\\Shirley Heather\\Desktop\\UBC\\future.txt', future_words)
