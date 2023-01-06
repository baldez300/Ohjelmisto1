
# Write a program that converts inches to centimeters until the user enters a negative number of inches.
# After that, the program stops working. '1 inch = 2.54 cm'


while True:
    inch_number = float(input("Give a number (inch): "))

    if inch_number > 0:
        print(f"{inch_number} inch = {inch_number * 2.54} cm")
    else:
        print("A negative or zero entry")
        break
