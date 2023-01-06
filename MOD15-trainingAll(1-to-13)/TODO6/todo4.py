import random


# Write a function that takes a list of integers as a parameter.
# The program returns the sum of the numbers in the list.
# For testing, write a main program where you create a list,
# call a function and print the sum it returns.


def sum_of_integers(num):
    return sum(num)


num_list = [1, 2, 3, 4, 5]
print(f"List: {num_list} \nSum: {sum_of_integers(num_list)}")


def sum2(number_list):  # Another way to do the task =================================
    return sum(number_list)


for i in range(2):
    numbers = []

    for length in range(5):
        numbers.append(random.randint(1, 10))
    print(f"\nList of numbers: {numbers} \nSum of numbers: {sum2(numbers)}")