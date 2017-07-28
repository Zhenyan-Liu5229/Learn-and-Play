#An interactive fiction game.
#It is about my experiences of Digital Literature workshops when I was on exchange to University of Otago, New Zealand in 2016. 
#I have wrote a paper draft of it as the final project of that course.
#The code I put here are based on the toturial from https://randomgeekery.org/post/2007/01-handling-a-single-round/.

def print_header():
    print('''
    _            _      _             _                  _     _        
   /_\  _ _     /_\  __| |_ _____ _ _| |_ _  _ _ _ ___  (_)_ _| |_ ___  
  / _ \| ' \   / _ \/ _` \ V / -_) ' \  _| || | '_/ -_) | | ' \  _/ _ \ 
 /_/_\_\_||_| /_/ \_\__,_|\_/\___|_||_\__|\_,_|_| \___| |_|_||_\__\___/ 
 |   \(_)__ _(_) |_ __ _| | | |  (_) |_ ___ _ _ __ _| |_ _  _ _ _ ___   
 | |) | / _` | |  _/ _` | | | |__| |  _/ -_) '_/ _` |  _| || | '_/ -_)  
 |___/|_\__, |_|\__\__,_|_| |____|_|\__\___|_| \__,_|\__|\_,_|_| \___|  
        |___/    
        ''')
print_header()
print('''
Welcome to An Adventure into Digital Literature!
You are one of students enrolled in ENG342 paper.
Now, your adventure start...''')

delay = input('>>> Press ENTER to start <<<')

from Scene import scenes
import sys
scene = scenes['beginning']
while True:
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
        scene = scenes[next_step['do']]
        a = str.lower(next_step['phrase'])
        print('You decide to',a,'.')