import random
def upgrade(x):
	return x+1
def d(x):
    return x*2    
a=0
n=15
exp=0
tok=0
I = ['D','L']
F = [10,11,12,12,13,13,14,14,15,15,16,16,17,17,19,19,20,20,21,22]
P = [1,1,1,10,11,12,12,13,13,14,14,15,15,16,16,17,17,19,19,20,20,21,22,'D','D','L','L','LE','LE','H','H']
while n > 0:
    S = random.choice(P)
    if S == 1:
        P[P.index(1)]=upgrade(1)
        exp=exp+960
        tok=tok+30        
    elif S == 2:
        P[P.index(2)]=upgrade(2)
        exp=exp+1200
        tok=tok+33
    elif S == 3:
        P[P.index(3)]=upgrade(3)
        exp=exp+1440
        tok=tok+36       
    elif S == 4:
        exp=exp+1780
        tok=tok+45
        P.remove(S)        
    elif S in F: 
        tok = tok+S*(2**a)
        P.remove(S)
    elif S == I[0]: 
        a=a+1
        P.remove(S)    
    elif S ==I[1]: 
        b = random.randint(1,9)
        tok = tok-b
        P.remove(S)
    else:
    	P.remove(S)
    print(exp,tok)
    n = n-1
tok = tok+200
exp = exp+2400
print('Investigation Complete. You\'ve got',exp,'Epx and',tok,'Token')
