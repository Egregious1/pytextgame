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

# path selection - keeping it simple now until I can figure out how to make it better
# this will only accept the inputs required but has no functin past verifying input atm


def choosePath():
    path = input('Do you go left or right? ("L" or "R"')
    if path == 'L' or path == 'l':
        print('You turn to your left and continue down your path')
    elif path == 'R' or path == 'r':
        print('You look to the path on your right and take it')
    else:
        if path != 'l' or path != 'L' or path != 'r' or path != 'R':
            choosePath()


startScreen()
print()
print()
print()
playerName = input('What is your name? ')
print()
print(f'Welcome {playerName}')
print()
displayIntro()
