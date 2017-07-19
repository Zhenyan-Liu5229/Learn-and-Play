scenes = {
    'beginning':{
    'description':'''You wake up. 
    It’s ten to one in the afternoon, a plain and dull Friday afternoon. 
    You are sitting in a computer lab, alone, with over thirty computers but no other fellow students. 
    You are very anxious because you are supposed to have the last workshop for ENG342 here. 
    No, there is no one. No Dave or David. 
    The computer in front of you requires your user name and password.
    ''',
    'paths':[
    {'do':'enter','phrase':'type your username'}
    ]
},
    'enter':{
    'description':'''As soon as you finish typing, the password appears automatically on the screen, and the computer unlocks. 
    Suddenly all the surroundings are gone.
    One hand reaches from the computer screen and drags you into it.
    ''',
    'paths':[
    {'do':'start','phrase':'look around'}
    ]
},
    'start':{
    'description':'''You are standing in the center of a mystic world.
    Around you are digital screens marked with numbers.
    There are four screens you can choose to look at.
    ''',
    'paths':[
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'No.2','phrase':'Look at No.2'},
    {'do':'No.3','phrase':'Look at No.3'},
    {'do':'No.10','phrase':'Look at No.10'}
    ]
},
    'No.7':{
    'description':'''You are playing The Stanley Parable. 
    Now your character, Stanley, is facing two open doors. 
    A loud male voice is repeating “Stanley chooses the door on his left”. 
    Are you going to obey him?
    ''',
    'paths':[
    {'do':'obey','phrase':'Move Stanley to the left door'},
    {'do':'disobey','phrase':'Move Stanley to the right door'}
    ]
},
    'obey':{
    'description':'''The voice is so compelling that you unconsciously obey him.
    You move Stanley through the left door. 
    You are in the world center again.
    ''',
    'paths':[
    {'do':'No.3','phrase':'Look at No.3'},
    {'do':'No.10','phrase':'Look at No.10'},
    {'do':'No.2','phrase':'Look at No.2'}
    ]
},
    'disobey':{
    'description':'''You are a person of strong free will.
    Obey a commanding stranger like him?
    Never!
    Stanley walks through the right door and never comes back.
    ''',
    'paths':[]
},
    'No.3':{
    'description':'''You are reading 253, a hypertext about a London underground train. 
    There is a map of passengers in car 2 of that train. 
    Each passenger has his/her interests written below his/her name.
    ''',
    'paths':[
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'No.10','phrase':'Look at No.10'},
    {'do':'No.2','phrase':'Look at No.2'},
    {'do':'No.6','phrase':'Look at No.6'}
    ]
},
    
    'No.2':{
    'description':'''You are writing a telescopic text. 
    For your sake, please do not lick here. 
    When you finish reading, screen No.2 is replaced by No.5.
    ''',
    'paths':[
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'No.10','phrase':'Look at No.10'},
    {'do':'No.3','phrase':'Look at No.3'},
    {'do':'No.5','phrase':'Look at No.5'}
    ]
},
    
    'No.5':{
    'description':'''You are playing Shadow of Colossus, an exciting PS4 game.
    This is the first time you play with a Joystick.
    Of course, you are not playing for fun.
    You need to write a 2500-word essay about it.
    ''',
    'paths':[
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'No.10','phrase':'Look at No.10'},
    {'do':'No.3','phrase':'Look at No.3'},
    ]
},
    
    'No.6':{
    'description':'''Another game? Yeah!
    This time you are playing The God of War.
    It is too hard to control the character.
    You are very distressed.
    So how about playing with texts instead of games?
    ''',
    'paths':[
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'No.10','phrase':'Look at No.10'},
    {'do':'No.9','phrase':'Look at No.9'},
    ]
},
    
    'No.9':{
    'description':'''Hey, isn't Interactive Fiction similar to RPGs?
    Can you solve the puzzle in Winchester's Nightmare?
    (Listen to the shell first!)
    Oh god, you spoil my game!
    ''',
    'paths':[
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'No.10','phrase':'Look at No.10'},
    {'do':'No.2','phrase':'Look at No.2'},
    ]
},
    
    'No.4':{
    'description':'''Poetry.
    You said to yourself.
    You are never going to like it.
    Although thoses flying words look funny.
    Although you,
    Cannot understand them.
    ''',
    
    'paths':[
    {'do':'No.2','phrase':'Look at No.2'},
    {'do':'No.10','phrase':'Look at No.10'},
    {'do':'No.3','phrase':'Look at No.3'},
    ]
},
    
    'No.10':{
    'description':'''Role-playing! I like it!
    Emmmm.How about a wood elf with a pet wolf?
    Wait, you there, you can't eat my wolf!
    And whoever pretending to be the god, I suppose you need a rest?
    ''',
    'paths':[
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'No.2','phrase':'Look at No.2'},
    {'do':'No.3','phrase':'Look at No.3'},
    {'do':'No.1','phrase':'Look at No.1'}
    ]
},
    
    'No.1':{
    'description':'''Well, the beginning of workshops.
    You are very nervous, because you know you are going to introduce yourself to other students.
    I am just an exchange student. What am I supposed to say?
    Surprisingly, Dave remembers your name after this very first class!
    ''',
    'paths':[
    {'do':'No.11','phrase':'Look at No.11'}
    ]
},
    
    'No.11':{
    'description':'''Welcome to the Final Web Project Assembly.
    You are taught to create links to other students'work.
    Is that the end? You ask yourself.
    'Yes, it is.'
    You have to leave.
    ''',
    'paths':[]
}
}
