#An interactive fiction game.
#It is about my experiences of Digital Literature workshops when I was on exchange to University of Otago, New Zealand in 2016. 
#I have wrote a paper draft of it as the final project of that course.
#The code I put here are based on the toturial from https://randomgeekery.org/post/2007/01-handling-a-single-round/.

scenes = {
    'No.7':{
    'description':'''You are playing The Stanley Parable. 
    Now your character, Stanley, is facing two open doors. 
    A loud male voice is repeating “Stanley chooses the door on his left”. 
    Are you going to obey him?''',
    'paths':[
    {'look_at':'No.3','phrase':'Look at No.3'},
    {'look_at':'No.10','phrase':'Look at No.10'},
    {'look_at':'No.2','phrase':'Look at No.2'}
    ]
},
    'No.3':{
    'description':'''You are reading 253, a hypertext about a London underground train. 
    There is a map of passengers in car 2 of that train. 
    Each passenger has his/her interests written below his/her name.''',
    'paths':[
    {'look_at':'No.7','phrase':'Look at No.7'},
    {'look_at':'No.10','phrase':'Look at No.10'},
    {'look_at':'No.2','phrase':'Look at No.2'},
    {'look_at':'No.6','phrase':'Look at No.6'}
    ]
},
    'No.2':{
    'description':'''You are writing a telescopic text. 
    For your sake, please do not lick here. 
    When you finish reading, screen No.2 is replaced by No.5.''',
    'paths':[
    {'look_at':'No.7','phrase':'Look at No.7'},
    {'look_at':'No.10','phrase':'Look at No.10'},
    {'look_at':'No.3','phrase':'Look at No.3'},
    {'look_at':'No.5','phrase':'Look at No.5'},
    ]
},
    'No.5':{
    'description':'''You are playing Shadow of Colossus, an exciting PS4 game.
    This is the first time you play with a Joystick.
    Of course, you are not playing for fun.
    You need to write a 2500-word essay about it.''',
    'paths':[
    {'look_at':'No.7','phrase':'Look at No.7'},
    {'look_at':'No.10','phrase':'Look at No.10'},
    {'look_at':'No.3','phrase':'Look at No.3'},
    ]
},
    'No.6':{
    'description':'''Another game? Yeah!
    This time you are playing The God of War.
    It is too hard to control the character.
    You are very distressed.
    So how about playing with texts instead of games?''',
    'paths':[
    {'look_at':'No.7','phrase':'Look at No.7'},
    {'look_at':'No.10','phrase':'Look at No.10'},
    {'look_at':'No.9','phrase':'Look at No.9'},
    ]
},
    'No.9':{
    'description':'''Hey, isn't Interactive Fiction similar to RPGs?
    Can you solve the puzzle in Lady Winchester's Nightmare?
    (Listen to the shell first!)
    Oh god, you spoil my game!''',
    'paths':[
    {'look_at':'No.7','phrase':'Look at No.7'},
    {'look_at':'No.10','phrase':'Look at No.10'},
    {'look_at':'No.2','phrase':'Look at No.2'},
    ]
},
    'No.4':{
    'description':'''Poetry.
    You said to yourself.
    You are never going to like it.
    Although thoses flying words look funny.
    Although you,
    Cannot understand them.''',
    'paths':[
    {'look_at':'No.2','phrase':'Look at No.2'},
    {'look_at':'No.10','phrase':'Look at No.10'},
    {'look_at':'No.3','phrase':'Look at No.3'},
    ]
},
    'No.10':{
    'description':'''Role-playing! I like it!
    Emmmm.How about a wood elf with a pet wolf?
    Wait, you there, you can't eat my wolf!
    And whoever pretending to be the god, I suppose you need a rest?''',
    'paths':[
    {'look_at':'No.7','phrase':'Look at No.7'},
    {'look_at':'No.2','phrase':'Look at No.2'},
    {'look_at':'No.3','phrase':'Look at No.3'},
    {'look_at':'No.1','phrase':'Look at No.1'}
    ]
},
    'No.1':{
    'description':'''Well, the beginning of workshops.
    You are very nervous, because you know you are going to introduce yourself to other students.
    I am just an exchange student. What am I supposed to say?
    Surprisingly, Dave remembers your name after this very first class!''',
    'paths':[
    {'look_at':'No.11','phrase':'Look at No.11'}
    ]
},
    'No.11':{
    'description':'''Welcome to the Final Web Project Assembly.
    You are taught to create links to other students'work.
    Is that the end? You ask yourself.
    'Yes, it is.'
    You have to leave.''',
    'paths':[]
},
    'Start':{
    'description':'''You are standing in the center of a mystic world.
Around you are various flying digital screens marked with numbers.
There are four screens you can choose to look at.''',
    'paths':[
    {'look_at':'No.7','phrase':'Look at No.7'},
    {'look_at':'No.2','phrase':'Look at No.2'},
    {'look_at':'No.3','phrase':'Look at No.3'},
    {'look_at':'No.10','phrase':'Look at No.10'}
    ]
}
}
import sys
scene = scenes['Start']
while 1 == 1:
    next_step = None    
    description = scene['description']
    paths  = scene['paths']
    print(scene['description'])

#Review the choices on board
    for i in range(0,len(paths)):
        path = paths[i]
        menu_item = i+1
        print(menu_item, path['phrase'])
    print('(0, To quit the game)')

#User selection
    prompt = 'Make a selection (0-%s):'%len(paths)
    while next_step == None:
        try:
            Step = input(prompt)
            menu_selection = int(Step)
            if menu_selection == 0:
                next_step = 'quit the game'
            else:
                index = menu_selection-1
                next_step = paths[index]
        except (IndexError,ValueError):
            print(Step,'is not a valid selection!',)
    if next_step == 'quit the game':
        print('You decide to',next_step,'.','Good Bye!')
        sys.exit()
    else:
        scene = scenes[next_step['look_at']]
        a = str.lower(next_step['phrase'])
        print('You decide to',a,'.')
