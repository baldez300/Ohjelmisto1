# Write a program that asks the user for the ship's cabin class (LUX, A, B, C)
# and prints its verbal description according to the list below.
# The task must use an if/elif/else repetition structure.
# LUX is a cabin with a balcony on the upper deck.
# A is a windowed cabin above the car deck.
# B is a windowless cabin above the car deck.
# C is a windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program prints 'Invalid cabin class'.

cabin_class = input("Select your cabin between(LUX, A, B or C): ").upper()

if cabin_class == 'LUX':
    print("LUX is a cabin with a balcony on the upper deck.")
elif cabin_class == 'A':
    print("A is a windowed cabin above the car deck.")
elif cabin_class == 'B':
    print("B is a windowless cabin above the car deck.")
elif cabin_class == 'C':
    print("C is a windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
