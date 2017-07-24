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
