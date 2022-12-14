# Pelin kaksi päätavoitetta ovat käydä kaikilla mantereilla/maanossa ja kerätä vähintään 10 lippua,
# mahdollisimman pienellä co2-päästöillä.

import mysql.connector
import geopy.distance
import flag


# 1 Connecting python to sql function
def connect_database():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user',
        password='password',
        autocommit=True
         )


connection = connect_database()


# 2 lentokenttien haku eri maista
def select_country(country):
    sql = f"select airport.name, ident from airport  inner join country on airport.iso_country = country.iso_country " \
          f"where country.name='{country}' and type in ('medium_airport', 'large_airport') order by rand() limit 5;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print(f"{i[0]}: {i[1]}")

    if not result:
        print("Anna kelvollinen maa")
    else:
        return result


# 3 maan lentokentän valinta
def select_country_airport(airport, iso):
    sql = f"select name from airport where ident='{airport}' and iso_country = '{iso}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print("\n------------------------")
        print(f"Olet nyt lentokentällä: {i[0]}")

    if not result:
        print("Anna kelvollinen lentokentän icao-koodi")
    else:
        return result


# 4 maiden haku
def search_country_in_continent(continent):
    sql = f"SELECT name FROM country where continent = '{continent}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    countrylist = []
    for i in result:
        print(i[0])
        countrylist.append(i[0])

    if not result:
        print("Anna kelvollinen maanosa")
    else:
        return countrylist


# 5 Maan iso_countryn hakeminen
def isocountry(country):
    sql = f"SELECT iso_country FROM country WHERE name = '{country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        isocode = i[0]

    return isocode


# 6 Lentokentän nimen hakeminen ainoastaan
def search_airport(icao):
    sql = f"SELECT name FROM airport where ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        text = i[0]

    return text


# 7 Lentokenttien gps sijainnit
def airport_location(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        lat = i[0]
        lon = i[1]
    location = (lat, lon)
    return location


# 8 Maaliin pääsyn tarkistus
def check_tickets_continents():
    sql = f"SELECT tickets_amount, continents_amount from game where screen_name = '{username}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    tickets = 0
    continent = 0
    for i in result:
        tickets = i[0]
        continent = i[1]

    return tickets, continent


# 9 Funktio luo käyttäjän tietokantaan
def createuser():
    sql = f"INSERT INTO game (screen_name) VALUES ('{username}')"
    cursor = connection.cursor()
    cursor.execute(sql)


# 10 Päivittää pelaajan sijaintia tietokantaan
def set_player_location(iso):
    sql = f"UPDATE game SET location = ('{iso.upper()}') WHERE screen_name = '{username}'"
    cursor = connection.cursor()
    cursor.execute(sql)


# 11 Lisää maanosan tietokantaan
def checkcontinent(userinput_1):
    if userinput_1 in checklist:
        checklist.remove(userinput_1)
        # print(checklist)
        sql = f"UPDATE game SET continents_amount = continents_amount + 1 WHERE screen_name = '{username}'"
        cursor = connection.cursor()
        cursor.execute(sql)


# 12 Hakee lipun
def get_flag(country):
    try:
        sql = f"SELECT iso_country FROM country WHERE country.name = '{country}';"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            codestr = "".join(i)
            countryflag = flag.flag(codestr)
            # flaglist.append(lippu)
            return countryflag
    except:
        print("Virheellinen syöte!")


# 13 Lisää yhden kerätyn lipun tietokantaan
def flags_counter():
    sql = f"UPDATE game SET tickets_amount = tickets_amount + 1 WHERE screen_name = '{username}'"
    cursor = connection.cursor()
    cursor.execute(sql)


# 14 Tarkistaa top5 listan ja ilmoittaa pääsikö käyttäjä sille ja tulostaa sen samalla jos pääsi
def top5check():
    sql = "SELECT screen_name, co2_consumed FROM game WHERE tickets_amount >= '10' " \
          "and continents_amount >='6' ORDER BY co2_consumed DESC LIMIT 5"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    names = []
    for name in result:
        names.append(name[0])
    if username in names:
        print("\nPääsit top 5 -listalle:\n")
        sql = "SELECT screen_name, co2_consumed FROM game " \
              "WHERE tickets_amount >= '10' and continents_amount >='6' ORDER BY co2_consumed ASC LIMIT 5"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        counter = 1
        for n in result:
            print(f"{counter}. Käyttäjänimi:", n[0], "\n ⤷ Pisteet:", n[1], "\n")
            counter += 1
    else:
        print("Et päässyt top 5 -listalle")


# 15 Päivittää co2
def co2update():
    sql = f"UPDATE game SET co2_consumed = ('{co2overallused}') WHERE screen_name = '{username}'"
    cursor = connection.cursor()
    cursor.execute(sql)


# 16 Tarkistaa löytyykö käyttäjänimi jo tietokannasta
def checkusername(useinput):
    sql = f"SELECT screen_name FROM game WHERE screen_name = '{useinput}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return result


# co2 päästöt kilogrammoina per kilometri
co2perkm = 0.225
# co2 kokonaispäästöt
co2overallused = 0

checklist = ["AF", "AS", "EU", "NA", "OC", "SA"]
flaglist = []
userloop = True

while userloop:
    try:
        usernameinput = input("Anna pelinimesi: ")
        username_check = checkusername(usernameinput)

        if username_check:
            print(f"Käyttäjänimi {usernameinput} on jo varattu!")
        if not username_check:
            username = usernameinput
            createuser()
            userloop = False
    except ValueError:
        print("Virheellinen syöte!")


print(f"""\nTervetuloa pelaamaan lentopeliä {username}.
Tarkoituksenasi on lentää kaikki maanosat läpi keräten maiden lippuja
mahdollisimman pienellä co2-päästöillä""")


# Itse pelin aloitus
print("""                      """)
print("------------------------")
print("""Helsinki-Vantaa --> EFHK
Enontekiö Airport --> EFET
Kokkola-Pietarsaari Airport --> EFKK""")
print("------------------------")
print("""                      """)

starticaos = ("EFHK", "EFET", "EFKK")

airport = ""

while airport not in starticaos:
    airport = input("Miltä lentokentältä haluat aloittaa?: ").upper()
    if airport not in starticaos:
        print("Anna joku yllämainituista icao-koodeista!")


set_player_location("fi")
start_airport = search_airport(airport)

count = "EU"
startcount = "EU"
print("""                      """)
print("------------------------")
print(f"Olet lentokentällä: {start_airport}")
print("------------------------\n")

# Loop through above functions to travel more.
program_running = True

while program_running:
    goal = check_tickets_continents()
    if goal[0] >= 10 and goal[1] >= 6:
        print("Olet kerännyt tarvittavan määrän lippuja sekä käynyt kaikissa maanosissa\n")
        print("Seuraavaksi voit lentää maaliin eli joihinkin aloitus pisteistä"
              "\n\nHelsinki-Vantaa --> EFHK "
              "\nEnontekiö --> EFET\n"
              "Kokkola-Pietarsaari --> EFKK")
        goalairport = ""
        while goalairport not in starticaos:
            goalairport = input("Mihin näistä haluat lentää?: ").upper()
            if goalairport not in starticaos:
                print("Sinun täytyy valita jokin aloitus lentokenttien ICAO-Koodeista")
        current_airport_location = airport_location(airport)
        next_airport_location = airport_location(goalairport)
        distance = geopy.distance.distance(current_airport_location, next_airport_location).km.__round__(2)
        airport = goalairport
        co2used = (distance * co2perkm).__round__(2)

        # co2overallused += co2used
        set_player_location("FI")
        co2update()
        print(f"\nLentosi co2 päästöt olivat {co2used} kg\n")
        print(f"Olet saapunut maaliin lentokentälle {search_airport(goalairport)}\n")
        print(f"Matkasi kokonaispäästöt olivat {co2overallused.__round__(2)} kg\n")
        print(f"Sait kerättyä {len(flaglist)} lippua:\n{flaglist}")
        top5check()
        program_running = False
    else:
        print("Jos haluat lentää saman maanosan sisällä syötä: Toiseen maahan"
              "\nJos haluat vaihtaa maanosaa syötä: Toiseen maanosaan"
              "\nKokonaispäästösi näet komennolla: Päästöt"
              "\nTop5-listan näet komennolla: top5"
              "\nKaikki keräämäsi liput näet komennolla: liput")
        print("------------------------")
        userinput = input("Mitä haluaisit tehdä?: ").lower()
        print("------------------------")
        if userinput == "päästöt":
            print(f"Kokonais co2 päästöstösi ovat {co2overallused.__round__(2)} kg")
            print("------------------------\n")
        elif userinput == "liput":
            print(f"Olet kerännyt {len(flaglist)} lippua:\n{flaglist}")
            print(f"Sinulta puuttuu vielä {10 - len(flaglist)} lippua tavoitteesta!")
            if goal[1] < 6:
                print(f"Sinulla on myös {6 - goal[1]} maanosaa käymättä!\n")

        elif userinput == "top5":
            print(f"Top 5 Lista:\n")
            sql_1 = "SELECT screen_name, co2_consumed FROM game WHERE tickets_amount >= '10' " \
                    "and continents_amount >='6' ORDER BY co2_consumed ASC LIMIT 5"
            cursor_1 = connection.cursor()
            cursor_1.execute(sql_1)
            result_1 = cursor_1.fetchall()
            counter_1 = 1
            for n_1 in result_1:
                print(f"{counter_1}. Käyttäjänimi:", n_1[0], "\n ⤷ Pisteet:", n_1[1], "\n")
                counter_1 += 1
            print("------------------------\n")
        elif userinput == "toiseen maanosaan":
            continentloop = []
            nameloop = []
            icaoloop = []
            while not continentloop:
                counts = ("AF", "AS", "EU", "NA", "OC", "SA")
                newcount = input("Valitse maanosan nimi AF(Africa), AS(Asia), EU(Europe), "
                                 "\n NA(North-America), OC(Oceania), SA(South-America): ").upper()
                if newcount == count:
                    print("Olet jo tässä maanosassa!")
                elif newcount in counts:
                    count = newcount
                    checkcontinent(count)
                    print("------------------------")
                    continentloop = search_country_in_continent(count)
                    print("------------------------")
                else:
                    print("Virheellinen syöte!")

            while not nameloop:
                countryNm = input("Anna sen maan nimi, johon haluat matkustaa: ")
                if countryNm in continentloop:
                    print("\n------------------------")
                    nameloop = select_country(countryNm)
                    print("------------------------\n")
                    flager = get_flag(countryNm)
                    if flager not in flaglist:
                        flaglist.append(flager)
                        flags_counter()
                    elif flager in flaglist:
                        print("Olet jo kerännyt tämän lipun!")

            while not icaoloop:
                try:
                    airportIcaoCode = input("Valitse yllä olevista satunnaisista lentokentistä "
                                            "kirjoittamalla ICAO-koodi: ")
                    iso_country = isocountry(countryNm)
                    icaoloop = select_country_airport(airportIcaoCode, iso_country)
                except ValueError:
                    print("Virheellinen Syöte!")

            current_airport_location = airport_location(airport)
            next_airport_location = airport_location(airportIcaoCode)
            distance = geopy.distance.distance(current_airport_location, next_airport_location).km.__round__(2)
            co2used = (distance * co2perkm).__round__(2)
            co2overallused += co2used
            print(f"\nMatka lentokentälle oli {distance} km")
            print(f"Co2 päästöjä syntyi {co2used} kg")
            print("------------------------")
            airport = airportIcaoCode
            set_player_location(iso_country)
            co2update()

        elif userinput == "toiseen maahan":
            countryloop = []
            icaoloop = []
            search_country_in_continent(count)
            print("------------------------\n")
            if startcount == "EU":
                checkcontinent(startcount)
                startcount = ""
            while not countryloop:
                try:
                    countryNm = input("Anna sen maan nimi, johon haluat matkustaa: ")
                    print("------------------------")
                    countryloop = select_country(countryNm)
                    print("------------------------")
                    flager = get_flag(countryNm)
                    if flager not in flaglist:
                        flaglist.append(flager)
                        flags_counter()
                    elif flager in flaglist:
                        print("Olet jo kerännyt tämän lipun!")
                except ValueError:
                    print("Virheellinen syöte")
            while not icaoloop:
                try:
                    iso_country = isocountry(countryNm)
                    airportIcaoCode = input("Valitse yllä olevista satunnaisista lentokentistä "
                                            "kirjoittamalla ICAO-koodi: ")
                    icaoloop = select_country_airport(airportIcaoCode, iso_country)
                    print("------------------------")
                    current_airport_location = airport_location(airport)
                    next_airport_location = airport_location(airportIcaoCode)
                    distance = geopy.distance.distance(current_airport_location, next_airport_location).km.__round__(2)
                    airport = airportIcaoCode
                    co2used = (distance * co2perkm).__round__(2)
                    co2overallused += co2used
                    print(f"\n Matka lentokentälle oli {distance} km")
                    print(f"Co2 päästöjä syntyi {co2used} kg")
                    print("------------------------")
                    airport = airportIcaoCode
                    set_player_location(iso_country)
                    co2update()
                except ValueError:
                    print("Virheellinen syöte")