import random


# Modify the previous function so that the function receives the total number of faces
# of the dice as a parameter. With the modified function, you can throw, for example,
# a 21-sided role-playing dice.
# In contrast to the previous task,
# the rolling of the dice is continued in the main program until the maximum
# eye count of the dice is obtained, which is asked from the user at the beginning of the program execution.

def dice_roll(sides):
    return random.randint(1, sides)


number_of_sides = int(input("Give number of sides to roll: "))
num_of_dice = None

while num_of_dice != number_of_sides:
    num_of_dice = dice_roll(number_of_sides)
    print(f"Dice rolled: {num_of_dice}")