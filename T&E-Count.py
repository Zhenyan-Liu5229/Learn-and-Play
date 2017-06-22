import random
n = 15
Token = 0
Exp = 0
F = [10,11,12,12,13,13,14,14,15,15,16,16,17,17,19,19,20,20,21,22]
L = ['E1','E2','E3','E4','F','D','L']
while n > 0:
    Step = input()
    if  Step == L[0]: #Enemy at First level
        Exp = Exp+960
        Token = Token+30
    elif Step == L[1]: #Enemy at Second level
        Exp = Exp+1200
        Token = Token+33
    elif Step == L[2]: #Enemy at Third level
        Token = Token+36
        Exp  = Exp+1440
    elif Step ==L[3]: #Enemy at Fourth level
        Token = Token+45
        Exp = Exp+1780
    elif Step ==L[4]: #Random select Token-Card
        a = random.choice(F)
        Token = Token+a
        F.remove(a)
    elif Step ==L[5]: #Double-Token Card selected
        def d(x):
            return x*2    
        DF = map(d,F)
        F = list(DF)
    elif Step ==L[6]: #Lose Tokens
        b = random.randint(1,9)
        Token = Token-b
    print(Token,Exp)
    n = n-1
Token = Token+200
Exp = Exp+2400
print('Investigation Complete. You\'ve got',Token,'Token and',Exp,'Exp')
