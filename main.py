import random

print("**** Welcome to the Guessing Game! *****")

#### Project Planning
# 1) Number Randomizer for computer
# 2) Loop for replaying
# 3) Conditionals to play again or evaluate players number vs. computers number
# 4) Provide user input for players number

print("I am computer. Guess my number")

computerNum = random.randint(0,20)
print(computerNum)

#state variables
win = False
still_playing = True
tries = 5

while still_playing == True:
    while tries > 0:
        print()
        playerNum = int(input("Enter a number between 0-20:   "))
        print(playerNum)


