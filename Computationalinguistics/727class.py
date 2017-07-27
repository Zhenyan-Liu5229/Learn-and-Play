#2017.7.27
#Hawaiian FSA
symbol = ['C','V']
state = ['q0','q1','q2']
transitions = {'q0':['q1','q2'],
              'q1':['q1','q2'],
              'q2':'q1'}

def transition(letters, current_state):
    current_state = 'q0'
    for letter in letters:
        if current_state == state[0]:
            if letter == symbol[0]:
                current_state = transitions[current_state][1]
            else:
                current_state = transitions[current_state][0]
        elif current_state == state[1]:
            if letter == symbol[0]:
                current_state = transitions[current_state][1]
            else:
                current_state = transitions[current_state][0]
        elif current_state == state[2]:
            if letter == symbol[1]:
                current_state = transitions[current_state]
            else:
                break   
    if current_state == 'q1':
        print('True')
    else:
        print('False')        

while True:   
    letters = input()
    transition(letters, 'q0')
