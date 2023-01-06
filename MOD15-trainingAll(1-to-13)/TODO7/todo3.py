
# Write a program to retrieve and store airport information.
# The program asks the user if he wants to enter a new airport,
# retrieve the information of an already entered airport, or stop.
# If the user chooses to enter a new airport, the program asks the user for the airport's ICAO code and name.
# If the user selects search, the program asks for the ICAO code and prints the corresponding airport name.
# If the user wants to stop, the execution of the program ends.
# The user can choose a new function as many times as they like, until they want to stop.
# (The ICAO code is the airport's unique identifier. For example, the ICAO code of Helsinki-Vantaa airport is EFHK.
# You can find the codes easily with a browser.)

# In this example you must first input the airport(s) icao code(s) and name(s)
airports = {}

while True:
    select = input("Do you want to enter a (new) airport, (search) an entered one or (stop)?: ")
    if select == "new":
        icao = input("Give the airport ICAO-code: ").upper()
        name = input("Give the airport name: ")
        if icao in airports:
            print("Airport exists already!")
        else:
            airports[icao] = name
    elif select == "search":
        if len(airports) == 0:  # See if dictionary is empty 'not airports', 'not bool(airports)' len(airports)==0
            print("Dictionary is empty")
            icao = input("Enter new airport ICAO-code: ").upper()
            name = input("Enter new airport name: ")
            if icao in airports:
                print("Airport exists already!")
            else:
                airports[icao] = name
        else:
            icao2 = input("Enter the ICAO-code: ").upper()
            print(airports[icao2])
    else:
        print("Airport not found")
        break


# In this example  the airports icao-codes and names are hard coded first, but you can add airports
def search_airport():
    icao = input("Write the ICAO-code: ").upper()
    if icao in air_ports:
        print("\n" * 5 + air_ports[icao])
    else:
        print("\n" * 5 + "Airport not found")


def add_airport():
    icao = input("Give airport ICAO-code: ").upper()
    name = input("Give airport name: ")
    if icao in air_ports:
        print("\n" * 5 + "Airport exists already!")
    else:
        air_ports[icao] = name
        print("\n" * 5 + "Airport added!")


air_ports = {
  "EFET":	"Enontekiön lentoasema",
  "EFHK":	"Helsinki-Vantaan lentoasema",
  "EFIV":	"Ivalon lentoasema",
  "EFJO":	"Joensuun lentoasema",
  "EFKI":	"Kajaanin lentoasema",
  "EFKE":	"Kemi-Tornion lentoasema",
  "EFKT":	"Kittilän lentoasema",
  "EFKK":	"Kokkola-Pietarsaaren lentoasema",
  "EFKS":	"Kuusamon lentoasema",
  "EFLP":	"Lappeenrannan lentoasema",
  "EFMA":	"Maarianhaminan lentoasema",
  "EFMI":	"Mikkelin lentoasema",
  "EFOU":	"Oulun lentoasema",
  "EFPO":	"Porin lentoasema",
  "EFSA":	"Savonlinnan lentoasema",
  "EFSI":	"Seinäjoen lentoasema",
  "EFTU":	"Turun lentoasema",
  "EFVA":	"Vaasan lentoasema"
}

while True:
    print("#"*3 + "$" * 50)
    print("1). Search airport through ICAO-code")
    print("2). Add airport")
    print("3). Stop")
    user_input = input("Write a number: ")

    if user_input == "1": search_airport()
    elif user_input == "2": add_airport()
    else: break