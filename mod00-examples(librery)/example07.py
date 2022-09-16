# Monikko, joukko ja sanakirja
num = 1
print(type(num))

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(type(numbers))
print(numbers)

for n in numbers:
    print(n)

# 1. alkio(tuple) ==========================
print(numbers[0])
numbers[0] = 9
print(numbers[0])

numbers = (1, 2, 3, 4, 5)
print(type(numbers))
print(numbers[0])
#numbers[0] = 9 <= ei onnistu
print(numbers[0])
for n in numbers:
    print(n)
print("-----\nJoukko\n")

# Joukko (set)
#inventory = {"valomiekka", "Pyssy", "kolikko", 3, numbers, False, True}
inventory = {"valomiekka", "Pyssy", "kolikko", "pyssy"}
print(inventory)
inventory.add("porkkana") # tehtave 07_2
inventory.remove("Pyssy")
print(inventory)
if "pyssy" in inventory: # tehtave 07_2 use while loop
    inventory.remove("pyssy")
else:
    print("Ei löytynyt pyssyä")
print(inventory)

# new_set = {} <= ei toimi
new_set = set()
print(type(new_set))
new_set.add("item 1")
new_set.add("item 2")
for item in new_set:
    print(item)
# Joukon koko (eli pituus) samoin kuin listoilla
print(len(new_set))

# Sanakirja (dictionary)
phone_numbers = {"Aku": "0404-2134567", "Minni": "045-9876543"}
# Listään uusi
phone_numbers["Viivi"] = "050-12345678"
print("1", phone_numbers)
# print(f"Akun numero:  {phone_numbers["Aku"]}) (f-strin)
print("Akun numero", phone_numbers["Aku"])
# Sijoitetaan vaimella 'aku' sama sam arvo, joka löytyy avaimella 'Viivi'
# Huom. kirjainkoko 'aku' vs 'Aku'
phone_numbers["aku"] = phone_numbers["Viivi"]
print("2", phone_numbers)

for n in phone_numbers:
    print(f'Avaimella ' + n + ' palutuu arvo ' + phone_numbers[n])


"""" # T 7.3. Runko
def add_airport():
    # TODO: ask & add airport airports dictionary

def search_airport():
    # TODO: ask for search string (key) & print value from airport dic

aiports = {}
program_running = True

while program_running:
    useinput = ""
    # TODO: input user command
    if useinput == 'lopeta':
        # quit app
    elif useinput == 'lisää':
        add_airport()
    elif useinput == 'hae':
        serch_airport() """


"""input_range = int(input("Give the range for your input: "))
    for i in range(input_range):
        icao_name = input("Anna ICAO-koodi: ")
        airport_name = input("Anna Lentoaseman nimi: ")

        airports[icao_name] = airport_name
    print(airports)"""
