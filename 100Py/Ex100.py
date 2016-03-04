"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right.
Keep the game going until the user types "exit"
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

secret = random.randint(1,9)
guess = 0
count = 0

print "Guess a number between 1 and 9"
while guess != secret and guess != "exit":
    guess = input("What's your guess?")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("That's correct, and it took you",count,"tries!")