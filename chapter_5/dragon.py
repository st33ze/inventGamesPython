# In this game the player is in a land full of dragons. The dragons all live in
# caves with their large piles of collected treasure. Some dragons are friendly
# and share their treasure. Other dragons are hungry and eat anyone who
# enters their cave. Tha player aproaches two caves, one with friendly dragon
# and one with hungry one, but doesn't know which dragon is in which cave.
# The player must choose between the two.

import random
import time

def main():
    playAgain = 'yes'
    while playAgain.lower() == 'yes' or playAgain.lower() == 'y':
        printIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
        playAgain = input('To play again type "yes or "y": ')


def printIntro():
    print(
    ''' You are in a land full of dragons. In front of you, you see two
    caves. In one cave, the dragon is friendly and will share his
    treasure with you. The other dragon is greedy and hungry, and will
    eat you on sight.''')
    print()

def chooseCave():
    # Returns cave number 1 or 2
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave you will go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(caveNumber):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky')
    time.sleep(2)
    print('A large dragon jumps in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyDragon = random.randint(1, 2)

    if friendlyDragon == int(caveNumber):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')



if __name__ == '__main__':
    main()
