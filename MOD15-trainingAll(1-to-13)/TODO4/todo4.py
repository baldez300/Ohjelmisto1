import random

# Write a game where the computer draws a number between 1..10.
# The machine guesses the number from the player until the player guesses correctly.
# After each guess, the program prints the text 'Too big guess', 'Too small guess' or 'Right'.
# Note that the computer must not change its number between guesses.

result = random.randint(1, 10)

while True:
    guess = int(input("Guess a number: "))
    if guess == result:
        print("Right")
        break
    elif guess < result:
        print("Too small guess")
    else:
        print("Too big guess")