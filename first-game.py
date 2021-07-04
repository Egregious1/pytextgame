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

# putting different rooms in this section


def smellyMareintro():
    print()
    print('From outside you can hear the whole tavern is a buzz with life,')
    print('as you take your first steps towards the door an arguing couple shuffles out of the door')
    print('The doors open wide and you are greeted with a blast of warmth and voices')
    print('The sound of merryment and music can beheard loudly in the streets.')
    print('you enter the Smelly Mare unsure what to expect')
    print('At the entrance a large breasted wench greets you with a smile as sweet as sin and with a voice to match says to you,')
    print('"Welcome to the Smelly Mare, where the drinks are stiff and the woman are loose!"')
    print('"The name is Gilda, and you are?"')
    print('You tell her your name and the she asks,')
    gildaMare()

# gilda interaction function going to keep it simple but without the just y/n questions and give some kind of choice. this will also help avoid repeating the intro.


def gildaMare():
    print('"what can I do you for a drink, a room, a lady, or all three?"')
    gilda = input('"what will it be (Drink, Lady, Room, or Info)?" ')
    if gilda == 'Drink' or gilda == 'drink':
        print(f'"Here ya go {playerName}!" Gilda slides you a tankard of some sweet smelling foaming liquid that you quickly drink down after one small sip.')
        print('You feel loads better than you did before.')
        print()
        gildaMare()
    elif gilda == 'Lady' or gilda == 'lady':
        print('"A woman eh? It might be hard to find one for someone with no reputation after all, but I have been known to make wonders happen."')
        print()
        gildaMare()
    elif gilda == 'room' or gilda == 'Room':
        print('"We have the finest rooms in all of Ravenwood even if we are the ONLY inn in Ravenwood"')
        print()
        gildaMare()
    elif gilda == 'info' or gilda == 'Info':
        print('I do have a wee problem that could use some help from someone like yourself...')
        print()
        gildaQuest()
        # insert some code to move on to the next function here
    else:
        if gilda != "Drink" or gilda != 'drink' or gilda != 'Lady' or gilda != 'lady' or gilda != 'room' or gilda != 'Room' or gilda != 'info' or gilda != 'Info':
            gildaMare()

#start of gilda's quest line
def gildaQuest():
    print('Glida motions you to follow her away from the door.')
    print('Gilda turns around and begins')
    print(f'"Okay {playerName}, I dont why but I feel like I can trust you with this.')
    print('Down in the cellar we have a bit of a problem..."')
    print()
    print('"Rats, big ones, one of unusual size to be exact"')
    print('"I just need you to go down there and take care of them for me yeah? If you take of this for me Ill take care of you later."')
    print('With a wink she turns around and smiles at you over her shoulder')
    print('"Just come back to me when youre done hun."')


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

def marketplaceIntro():
    print()
    print('As you make your way down to the end of the path the sweet smell of baked goods fills the air and you can hear all sorts of people buying and selling wares')
    print('you pass by all sorts of small shops from fishmongers to brewers and even a small oddities shop.')
    print('One sign in particular catches your eye. A small sign sitting outside a dark hut that says')
    print('"do some shit for me you asshole"')
    print('you wonder what this could be so you step inside.')


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
print('to your right you see the market place.')
print()
print('Which way do you go? (L or R?)')
introPath()
