
# Write a program that asks the user for the names of five cities one at a time
# (use a 'for loop structure' to ask for the names) and store them in a list structure.
# Finally, the program prints the names of the cities one by one below in the same order as they were entered.
# Use the for iteration structure to query the names and the 'for/in' iteration structure to iterate through them.

cities = []

for i in range(5):
    city_name = input("Enter a city name: ")
    cities.append(city_name)

for city in cities:
    print(f"\n{city}")
