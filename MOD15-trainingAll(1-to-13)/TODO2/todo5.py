from math import floor

# Write a program that asks the user for the medieval measurements of mass in loaves, nails, and bullets.
# The program converts the input into full kilograms and grams and informs the user of the result.
#
# One loave is 20 pounds.
# One nail is 32 bullets.
# One bullet is 13.3 grams.
# An example of how the program works:
#
# Give the breadsticks.
# 3
#
# Give me the nails.
# 9
#
# Give me the bullets.
# 13.5
#
# Mass according to current measurements:
# 29 kilograms and 545.95 grams.

loave = float(input("Give the breadsticks in number: "))
nail = float(input("Give the nails in number: ")) + loave * 20
bullet = float(input("Give the bullets in number: ")) + nail * 32
gram = bullet * 13.3
kilo = floor(gram / 1000)

print(f"Mass according to current measurement: ")
print(f"{kilo} kilograms and {gram % 1000:.2f} grams.")