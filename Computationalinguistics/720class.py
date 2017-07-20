#2017.7.20
#dic
languages={'English':['Canada','USA','UK'],
            'French':['France','Canada','Senegal'],
            'Portugese':['Portugal','Brzail','Macau']}
print(languages['English'])
for name in languages:
    print(name)
    print(languages[name])
languages['Irish']=['Ireland']
print(languages)

#practice
likes={'Yi,Xin':'noodles',
       'Charles':'ramen',
       'Liza':'pizza',
       'Graham':'hotpot',
       'Anatas':'rice'}
for name in likes:
    print(name,'\'s favorite food is ',likes[name]) #likes[name]means the vaule of the key

#string spiltting and joining
digits = '1-800-567-2323'
breakup=digits.split('-')
print(breakup)

country='1'
aera='209'
phone='-'.join([country,aera])
print(phone)

#practice count syllable into a dictionary
syllable={}
words=['va.in.i','ka.jo.a','ja.o.o.ro','go.a','ko.a','a.fo.ro.ni','bo.vi.ri','ka.jo.vi.ri','a.ha.ka.ba.ra','so.hi.ri.ba.na.ki']
for word in words:
    break_word=word.split('.')
    for break_sy in break_word:
        if break_sy in syllable: 
            syllable[break_sy]=syllable[break_sy]+1
        else:
            syllable[break_sy]=1
print(syllable)
for syl in syllable:
    print('The syllable',syl,'occurs',syllable[syl],'times.') #the output is randomly presented

#capitalize the word stress
for word in words:
    break_word=word.split('.')
    syllable_length=len(break_word)
    if syllable_length<3: #lf len(word.split('.'))<3 three in one code
        break_word[-1]=break_word[-1].upper() #replace the old 
    else:
        break_word[-3]=break_word[-3].upper()
    word='.'.join(break_word)
    print(word)

#Boolean types (T/F)
words=['hongas',   
      'nyuah',   
      'mati',    
      'ju', 
      'pukul',   
      'buru',   
      'paca',   
      'tari',   
      'dongi',  
      'nyanyi',  
      'jual',   
      'poros',  
      'karu',   
      'muntah', 
      'cawako']
vowel=['a','i','e','o','u']
for word in words:
    if word[0] in ['p','b']:
        prefix='ngam'
        if word[0]=='p':
            word=prefix+word[1:]
        else:
            word=prefix+word
    elif word[0] in ['t','d']:
        prefix='ngan'
        if word[0]=='t':
            word=prefix+word[1:]
        else:
            word=prefix+word        
    elif word[0] in [vowel,'k']:
        prefix='ng'
        if word[0]=='k':
            word=prefix+word[1:]
        else:
            word=prefix+word
    elif word[0] in ['c','j','s']:
        prefix='ngnay'
        word=prefix+word
    else:
        prefix='nga' 
        word=prefix+word  
    print(word)

#open file
path='D:\\code\\PWL.txt'
file = open(path)
words = []
for line in file:
    line = line.strip()
    line = line.split('\t')
    line = line[0]
    words.append(line)
file.close()
