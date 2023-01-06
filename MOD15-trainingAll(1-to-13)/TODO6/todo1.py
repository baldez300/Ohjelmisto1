import random


# Write a parameterless function that returns as its return value a random dice number between 1..6.
# Write a main program that rolls the dice until a six comes up.
# The main program prints the number of stitches obtained after each throw.

def dice_roll():
    return random.randint(1, 6)


dice_number = None

while dice_number != 6:
    dice_number = dice_roll()
    print(f"Dice rolled: {dice_number}")