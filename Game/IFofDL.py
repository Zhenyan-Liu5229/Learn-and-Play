#An interactive fiction game.
#It is about my experiences of Digital Literature workshops when I was on exchange to University of Otago, New Zealand in 2016. 
#I have wrote a paper draft of it as the final project of that course.
#The code I put here are based on the toturial from https://randomgeekery.org/post/2007/01-handling-a-single-round/.

description  = '''
You are standing in the center of a mystic world.
Around you are various flying digital screens marked with numbers.
There are four screens you can choose to look at.'''
print(description)

#List of choices
paths = ['Look at No.7',
'Look at No.3',
'Look at No.10',
'Look at No.2']

#Review the choices on board
for i in range(0,len(paths)):
    path = paths[i]
    menu_item = i+1
    print(menu_item, path)
print('(0, To quit the game)')

#User selection
next_step = None
while next_step == None:
    try:
        Step = input('Make a selection:')
        menu_selection = int(Step)
        if menu_selection == 0:
            next_step = 'quit the game'
        else:
            index = menu_selection-1
            next_step = paths[index]
            print(menu_selection,'-',next_step)
    except (IndexError,ValueError):
        print(Step,'is not a valid selection!',)
if next_step == 'quit the game':
    print('You decide to',next_step,'.','Good Bye!')
else:
    a = str.lower(next_step)
    print('You decide to',a,'.')
