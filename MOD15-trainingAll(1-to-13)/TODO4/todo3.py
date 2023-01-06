
# Write a program that prompts the user for numbers until the user enters an empty string as an end character.
# Finally, the program prints the smallest and largest of the obtained numbers.

list_of_numbers = []

while True:
    number = input("Give a number (Ex.1): ")
    if number == "":
        break
    try:
        f_number = float(number)
    except:
        print("Invalid input")
        continue

    list_of_numbers.append(f_number)

    smallest_number = min(list_of_numbers)
    largest_number = max(list_of_numbers)
    print(f"No.1 The smallest number is: {smallest_number} and the largest number is: {largest_number}")

# Second option to do the same thing =====================================================
min_value = None
max_value = None

while True:
    num_string = input("Give a number (Ex.2): ")
    if num_string == "":
        break

    num_Int = int(num_string)
    if min_value is None or min_value > num_Int:
        min_value = num_Int
    if max_value is None or max_value < num_Int:
        max_value = num_Int

    if min_value is None:
        print("Invalid input")
    else:
        print(f"No.2 The smallest number is: {min_value} and the largest number is: {max_value}")
