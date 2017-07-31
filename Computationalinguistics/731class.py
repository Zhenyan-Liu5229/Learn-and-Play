#2017.7.31
#tuple immutable
pair = ('a','b')
a = ('B',) #need this comma

#id
s = 'ert'
print(id(s))

#decision-tree
file = open('D:\\code\\UBC\\1.txt', encoding = 'utf-8')
text = [line.strip() for line in file]
file.close()

for line in text:
    if 'č'in line:
        print('Czech')
        break
    elif 'π' in line:
        print('Greek')
        break
    elif 'ħ' in line:
        print('Maltese')
        break
    elif 'и' in line:
        print('Russian')
        break
    elif 'å' in line:
        print('Swedish')
        break
    elif '的' in line:
        if 'す' in line:
            print('Japanese')
            break
        else:
            print('Chinese')
            break
    elif 'qi' in line:
        print('Xhosa')
        break
    elif 'yw' in line:
        print('Welsh')
        break
    else:
        print('English or other languages')
        break
