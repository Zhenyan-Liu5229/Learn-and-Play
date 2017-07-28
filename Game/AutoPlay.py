import random   
a=0
n=14 #Steps in total
exp=0
tok=0
influence = ['D','L'] #Factors that influence token number. 'D'represents 'double' and 'L'represents 'loss'.
flower = [10,11,12,12,13,13,14,14,15,15,16,16,17,17,19,19,20,20,21,22]
pool = [1,1,1,10,11,12,12,13,13,14,14,15,15,16,16,17,17,19,19,20,20,21,22,'D','D','L','L','LE','LE','H','H'] #The pool of cards. 'LE'represents 'lose equipment' and 'H' represents 'hit damage'. 
while n > 0:
    selection = random.choice(pool)
    if selection == 1:
        pool[pool.index(1)]=2 #After the first battle, the enemy will level up. The highest level is the 4th.
        exp=exp+960
        tok=tok+30        
    elif selection == 2:
        pool[[pool.index(2)]=3 #level 2
        exp=exp+1200
        tok=tok+33
    elif selection == 3:
        pool[pool.index(3)]=4 #level 3
        exp=exp+1440
        tok=tok+36       
    elif selection == 4: #level 4
        exp=exp+1780
        tok=tok+45
        pool.remove(selection)        
    elif selection in flower: 
        tok = tok+selection*(2**a)
        pool.remove(selection)
    elif selection == influence[0]: 
        a=a+1
        pool.remove(selection)    
    elif selection == influence[1]: 
        b = random.randint(1,9)
        tok = tok-b
        pool.remove(selection)
    else:
    	pool.remove(selection)
    print(exp,tok)
    n = n-1
tok = tok+200
exp = exp+2400
print('Investigation Complete. You\'ve got',exp,'Epx and',tok,'Token')
