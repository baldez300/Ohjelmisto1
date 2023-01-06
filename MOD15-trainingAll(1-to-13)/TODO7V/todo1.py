
# For training

list_of_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

try:
    list_of_days[5] = "Saturday"
except TypeError as e:
    print("An error occurs:", e)

for day in list_of_days:
    print(day)

cent = {"Coin", "Wand", "Armor", "Amulet", "Coin", "Studs"}
print(cent)

cent = {(1, 2), (1, 2), (1, 2, 3)}
print(cent)
cent.add("Coin")
print(cent)
try:
    cent.remove(10_000)
except KeyError as e:
    print("Another error occurs:", e)

if "Coin" in cent:
    print("Coin found")