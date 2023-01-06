
# Write a program that asks the user for the number of the month,
# after which the program prints the corresponding season (spring, summer, autumn, winter).
# In your program, store the seasons corresponding to months as strings in a tuple data structure.
# Let's define each season as three months long, so that December is the first winter month.

seasons = ("Spring", "summer", "autumn", "winter")
month = int(input("Enter the month number(1 - 12): "))

if month == 3 or month == 4 or month == 5:
    print(seasons[0])
elif month == 6 or month == 7 or month == 8:
    print(seasons[1])
elif month == 9 or month == 10 or month == 11:
    print(seasons[2])
elif month == 12 or month == 1 or month == 2:
    print(seasons[3])
else:
    print("Invalid month number")


# Another way to do it
seasons_2 = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer",
             "autumn", "autumn", "autumn", "winter",)
month_number = int(input("Enter the month number(1-12)again: "))
print("The season of the year is:", seasons_2[month_number - 1])

