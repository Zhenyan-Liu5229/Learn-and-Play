#unicode
a = '[\u006D\u00E6\u0283\u026A\u014B]'
print(a)

#decision trees
file = open('D:\\code\\UBC\\language_ID(1).csv')

lines = []

for line in file:
    line = line.strip()
    lines.apppend(line) 
file.close()   
    
data = []
for index.line in enumerate(lines):
    line = line.split(',')
    data.append(({headers[n]:1
                 }))
