
# Write a function that receives as a parameter the amount of gasoline in US liquid gallons
# and returns the corresponding number of liters as its return value.
# Write a main program that prompts the user for the number of gallons and converts it to liters.
# The conversion must be done using a subprogram.
# The conversion continues until the user enters a negative number of gallons.
# One gallon is 3.785 liters.

def convert_gallon_to_liter(gallons):
    return gallons * 3.78541178


while True:
    gasoline_gallon = float(input("Enter the gallon amount: "))

    if gasoline_gallon >= 0:
        print(f"{gasoline_gallon} gallon(s) is/are {convert_gallon_to_liter(gasoline_gallon):.2f} liter(s)")
    else:
        print("Stop the operation.")
        break