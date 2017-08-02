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
