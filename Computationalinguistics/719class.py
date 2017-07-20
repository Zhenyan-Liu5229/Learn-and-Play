#2017.7.19
print('Hello World!')
a=42
print(a)
print('1.5+1.5')
print('1'+'1')
print(type('1'))#get the type
print('1'+'Alice')#concatenation
print('The number is,',a)

name='Yi,Xin'
gender='she'
age=20
print('My new friend is',name,'and',gender,'is',age,'years old.') 
print('My new friend is %s and %s is %s years old.'%(name,gender,age))

vowels=['a','i','e','u','o']
inventory=[vowels,'p','t']
print(inventory)
for v in vowels: #for-loops
    print(v)
word='paga'
for letter in word:
    print(letter)
#numbers are not iteratble
for a in range (1,10):
    print(a)

name=['Yi,Xin','Charles Pan','Grahan','Luo,Longjun','Liza']
for n in name:
    print(n,'is sitting at the table with me.' )

x=7
y=5
if x<y:
    print('x is less than y') #for string, check alphabatic order
elif x==y:
    print('x is equal to y')
else:
    print('x is greater than y')

rwords=['gago','huti','tagu','sisi','ga\'a','maui','magu','manaha','a\'u','momoe'] #some voca in Rennellese
for rword in rwords:
    count=0
    for letter in rword:
        if letter in vowels:
            count=count+1
    print(rword,'has', count,'syllables')
