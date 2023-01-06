import random


# Write a function that takes a list of integers as a parameter.
# The program returns another list, which is otherwise similar to the list received as a parameter,
# except that all odd numbers have been removed from it.
# For testing, write a main program in which you create a list,
# call a function, and then print both the original and the trimmed list.

def filter_odd_numbers(list_nums):
    return [num for num in list_nums if num % 2 == 0]


numbers = []
for length in range(10):
    numbers.append(random.randint(1, 100))
print(f"Original list: {numbers} \nList of even numbers: {filter_odd_numbers(numbers)}")
