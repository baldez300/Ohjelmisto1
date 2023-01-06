
# Write a program that prompts the user for names until the user enters an empty string.
# After entering each name, the program prints either the text 'New name'
# or 'Previously entered name', depending on whether the name was entered for the first time.
# Finally, the program lists the entered names one by one in an arbitrary order.
# Use an array data structure to store names.

names = set()

while True:
    user_name = input("Give a name: ")

    if user_name == "":
        print("You entered blank")
        break
    elif user_name in names:
        print("Previously entered name")
    else:
        print("New name")
        names.add(user_name)
        continue

for name in names:
    print(name)
