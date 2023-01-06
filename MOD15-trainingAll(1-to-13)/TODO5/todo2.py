
# Write a program that prompts the user for numbers until the user enters an empty string as an end character.
# Finally, the program prints the five largest numbers from the obtained numbers, starting with the largest.
# Hint: the sorting order of the elements in the list can be reversed by giving 'reverse=True' as an argument
# to the 'sort method'.

list_of_nums = []

while True:
    num = input("Give a number: ")

    if num == "":
        break

    list_of_nums.append(int(num))

list_of_nums.sort(reverse=True)
print(f"List of 5 numbers from largest to the smallest {list_of_nums[:5]}")