#An interactive fiction game.
#It is about my experiences of Digital Literature workshops when I was on exchange to University of Otago, New Zealand in 2016. 
#I have wrote a paper draft of it as the final project of that course.
#The code I put here are based on the toturial from https://randomgeekery.org/post/2007/01-handling-a-single-round/.

from Scene import scenes
import sys
import random

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

def readstatus(screens): #for users to check which contents they have read
    if screens not in read_status:
    	read_status.append(screens)
    return(read_status)

read_status = []
numbers = [1,2,3,4,5,6,7,9,10] #The number of each screen

#start of the game    
print_header()
print('''

Welcome to An Adventure into Digital Literature!
You are one of students enrolled in ENG342 paper.
Now, your adventure starts...
''')

delay = input('>>> Press ENTER to start <<<')


#the default beginning scene
scene = scenes['beginning'] #notice: the scene is actually scenes[scene] instead of the name of that sence
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
    print('\n(r, To view what you have read)\n(0, To quit the game)')


#User selection
    prompt = 'Make a selection (0-%s):' %len(paths)
    while next_step == None:
        try:
            step = input(prompt)
            if step == 'r': #allow player to see which one he/she has read
                print('''*************************************
-- You have read %s''' %read_status)            
            else: 
                menu_selection = int(step)   
                if menu_selection == 0:
                    next_step = 'quit the game'
                else:
                    index = menu_selection-1
                    next_step = paths[index]
        except (IndexError,ValueError):
            print(step,'is not a valid selection!',)

    if next_step == 'quit the game':
        print('\nYou decide to %s. Good Bye!' %next_step)
        sys.exit()
    else:
        scene = scenes[next_step['do']]
        next_phrase = str.lower(next_step['phrase'])
        readstatus(next_step['do'])
        print('''*************************************
You decide to''', next_phrase, '.')
        
        #add random mode (2017.8.21)
        if scene == {}:
            screen_number = random.choice(numbers)
            numbers.remove(screen_number)
            new_screen = 'No.'+ str(screen_number)
            scene = scenes[new_screen]
            readstatus(new_screen)
            if numbers == []:
            	scene = scenes['No.11']
            	readstatus('No.11')
