change = {'b':1,'f':1, 'p':1, 'v':1,
          'c':2,'g':2,'j':2,'k':2,'q':2,'s':2,'x':2,'z':2,
          'd':3,'t':3,
          'l':4,
          'm':5,'n':5,
          'r':6}
deletion = ['a','e','h','i','o','u','w','y']  

def fst(name):
    numbers = []
    final = []
    final_symbol = []

    for letter in name[1:]:
        numbers.append(change[letter] if letter in change
                        else letter)

    for i, number in enumerate(numbers):
        try:
            if not number == numbers[i-1]:
                final.append(number)
        except IndexError:
            pass

    final = [x for x in final if x not in deletion]

    final_symbol = list(map(str, final))
    
    # for number in final:
    #     number = str(number)
    #     final_symbol.append(number)

    while len(final_symbol) < 3:
        final_symbol.append('0')

    final_word = name[0] + ''.join(final_symbol)

    print(final_word[:4])

fst('Carlos')
