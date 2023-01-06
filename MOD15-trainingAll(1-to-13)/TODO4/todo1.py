
# Write a program using the while loop structure
# that prints numbers between 1..1000 that are divisible by three.

number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
