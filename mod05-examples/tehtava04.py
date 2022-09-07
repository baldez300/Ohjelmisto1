# Ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan
# allekkain samassa järjestyksessä kuin ne syötettiin.

city_list = []
city = int(input("Enter the size of the city list (5): "))

print("\n")
for i in range(0, city):
    print("Enter city name at index", i)
    item = input(": ")
    city_list.append(item)
print("Cities list is: ", city_list)
# Cities name one by one below in the same order as they were entered.
for n in city_list:
    print(f"{n}!")