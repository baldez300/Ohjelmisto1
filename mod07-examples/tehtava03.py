# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun,
# ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
# ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

def add_airport():
    # ask & add airports to dictionary
    # Ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen ja lisää ne lentokenttien sanakirjaan.
    go = True
    while go:
        icao_name = input("Anna ICAO-koodi: ")
        airport_name = input("Anna Lentoaseman nimi: ")

        airports[icao_name] = airport_name
        if icao_name == "" or airport_name == "":
            print(airports)
            break


def search_airport():
    # ask for search string (key) & print value from airport dictionary
    # Ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
    airports_list = {"EFHK": "Helsinki-Vantaan lentoasema", "EFOU": "Oulun lentoasema", "EFJY": "Jyväskylän lentoasema",
                     "efhk": "Helsinki-Vantaan lentoasema", "efou": "Oulun lentoasema", "efjy": "Jyväskylän lentoasema"}

    icao_code = input("Anna ICAO-koodi kirjaimilla(EFHK, EFOU tai EFJY): ")
    if icao_code in airports_list:
        print(f"ICAO-koodi: {icao_code} on: {airports_list[icao_code]}.")
    else:
        print("ICAO-koodia ei ole olemassa 'lisää' se luetteloon tai 'hae' uudelleen")


airports = {}
program_running = True

while program_running:
    # userinput = ""
    # input user command
    userinput = input("Anna 'lopeta', 'lisää' vai 'hae': ")
    if userinput == 'lopeta':
        print("Moikka ja tervetuloa uudelleen..!")
        break
    elif userinput == 'lisää':
        add_airport()
    elif userinput == 'hae':
        search_airport()