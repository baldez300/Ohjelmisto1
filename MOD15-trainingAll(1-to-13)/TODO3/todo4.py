
# Write a program that asks for the year and reports whether the given year is a leap year.
# A year is a leap year if it is divisible by four.
# Years divisible by one hundred are leap years only if they are also divisible by four hundred.

leap_year = int(input("Give a leap year: "))

if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
    print(f"{leap_year} is a leap year!")
else:
    print(f"{leap_year} is not a leap year!\n Try again..!")