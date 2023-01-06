import random

# Write a program that asks the user for the number of lottery cubes.
# The program throws all the dice once and prints the sum of the numbers.
# Use the for loop structure.

dice_count = int(input("How many dice are thrown?: "))
list_sum_of_all_dice = []

for i in range(dice_count):
    dice = random.randint(1, 6)
    list_sum_of_all_dice.append(dice)

print(sum(list_sum_of_all_dice))  # The sum of all outputs
print(list_sum_of_all_dice)  # The array list of every single dice output