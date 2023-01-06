from math import ceil

# Write a program that prompts the user for an integer and indicates whether it is a prime number.
# In this task, prime numbers are numbers that are only divisible by 1 and itself.

# For example, the number 13 is a prime number
# because it can only be divided by the numbers 1 and 13 in such a way that the division is even.
# On the other hand, for example, the number 21 is not a prime number,
# because it can also be divided equally by the number 3 or the number 7.

num = int(input("Give a number: "))

for i in range(2, ceil(num / 2)):
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
else:
    print(f"{num} is prime number")