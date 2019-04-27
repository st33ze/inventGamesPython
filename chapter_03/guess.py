# This is "guess the number game". Program chooses number in given bracket
# and the player has to guess the value in limited number of tries.

import random

def main():
    # Initial values
    bottomBorder = 0
    topBorder = 20
    triesAllowed = 4 +  round((abs(topBorder) + abs(bottomBorder)) / 100)
    number = random.randint(bottomBorder, topBorder)

    # Welcome user
    print("Hello! What is your name?")
    userName = input("Name: ")
    if not userName:
        userName = "Buddy"
    print("Well {}, I am thinking of a number between {} and {}."
          .format(userName, bottomBorder, topBorder))
    print("Take a guess by typing an integer. Tries available: {}."
          .format(triesAllowed))

    # Guessing loop
    for i in range(triesAllowed):
        # Make sure user typed an integer
        while(True):
            userNumber = input("Number: ")
            try:
                userNumber = int(userNumber)
                break
            except:
                print("This is not an integer... Try again.")

        # Check the guess
        if userNumber > number:
            print("Your guess is to high. Tries left: {}."
                  .format(triesAllowed - (1 + i)))
        elif userNumber < number:
            print("Your guess is too low. Tries left: {}."
                  .format(triesAllowed - (1 + i)))
        else:
            return print("Good job, {}! You guessed my number in {} guesses."
                  .format(userName, i + 1))

    # Else user didn't guess
    print("Nope. The number I was thinking of was {}.".format(number))

if __name__ == "__main__":
    main()
