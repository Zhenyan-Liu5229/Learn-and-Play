#2017.7.27
#Hawaiian FSA
symbol = ['C','V']
state = ['q0','q1','q2']
transitions = {'q0':['q1','q2'],
              'q1':['q1','q2'],
              'q2':['q1']}

def transition(letters, current_state = state[0]):
    for letter in letters:
        if letter == symbol[0]:
            current_state = transitions[current_state][1]
            if letter == symbol[1]:
                current_state = transitions[current_state][0]
            else:
                break
        elif letter == symbol[1]:
            current_state = transitions[current_state][0]
            if letter ==symbol[0]:
                transition(letter)
                
        
    if current_state == state[1]:
        print('Ture')
    else:
        print('False')

while True:
    letters = input()
    transition(letters)
