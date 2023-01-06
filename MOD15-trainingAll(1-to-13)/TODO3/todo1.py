
# Write a program that asks the fisherman the length of the walleye in centimeters.
# If the pike is undersized, the program tells you to put the pike back into the lake,
# while informing the user how many centimeters are missing from the lowest allowed catch size.
# A walleye is undersized if its length is less than 37 cm.

size = float(input("Enter the size of your walleye/yellow pike or yellow pickerel (cm): "))

if size < 37:
    print(f"Your walleye is too pitiful, put it back in the sea and collect a {37 - size}cm longer walleye")
else:
    print("What a nice catch, your walleye is in correct size! 👍")