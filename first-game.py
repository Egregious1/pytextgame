#Name: Egregious1
#Date: 6-28-21
# description: text based game

# splash screen or logo for game...yeah it sucks for now
def startScreen():
    print('********************')
    print('*                  *')
    print('*  The shit birds  *')
    print('*      Cometh      *')
    print('*                  *')
    print('*                  *')
    print('*                  *')
    print('********************')
    print()

# display intro pretty self explanitory


def displayIntro():
    print('It has been years since you have last seen your home,')
    print('in that time many things have changed, including you.')
    print('You stand at the gates of Ravenwood in search of family')
    print('before you stands a large door with a man looking at you through a hole.')
    print('Who are you?')
    print(f'You call out, "It is I {playerName}, I have come back home!"')
    print(f'{playerName}?! Well why didnt you say so? Come in come in!')

#putting different rooms in this section
def smellyMareintro():
    print()
    print('From outside you can hear the whole tavern is a buzz with life,')
    print('as you take your first steps towards the door an arguing couple shuffles out of the door')
    print('The doors open wide and you are greeted with a blast of warmth and voices')
    print('The sound of merryment and music can beheard loudly in the streets.')
    print('you enter the Smelly Mare unsure what to expect')

# path selection - this code is going to suck but I need to write it for each room until I learn how to optimize it.

def introPath():
    path = input('Do you go left or right? ("L" or "R") ')
    if path == 'L' or path == 'l':
        print('You turn to your left towards the tavern')
        smellyMareintro()
    elif path == 'R' or path == 'r':
        print('You look to the path on your right and take it')
    else:
        if path != 'l' or path != 'L' or path != 'r' or path != 'R':
            introPath()


startScreen()
print()
print()
print()
playerName = input('What is your name? ')
print()
print(f'Welcome {playerName}')
print()
displayIntro()
print()
print('You step through the gates and to your surprise the town is quiter than expected.')
print('You look to your left and see the Smelly Mare the local inn')
print('to your right you see the town bizaar')
print()
print('Which way do you go? (L or R?)')
introPath()


