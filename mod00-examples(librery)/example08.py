# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.

# Creating mariadb user & password for application specific database (flight_game):
# CREATE USER IF NOT EXISTS 'user'@'localhost' IDENTIFIED BY 'password';
# GRANT ALL PRIVILEGES ON `flight_game`.* TO 'user'@'localhost';

import mysql.connector


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

def get_country(iso_code):
    sql = f"SELECT iso_country, name, wikipedia_link FROM country WHERE iso_country='{iso_code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    # haetaan vain yksi (=ensimmäinen) tulosrivi
    result = cursor.fetchone() # type of result: tuple
    print("koko tulos monikko:", result)
    print("tuloksia yhteensä:", cursor.rowcount)
    if cursor.rowcount > 0:
        print(f"{result[0]}: {result[1]}, wikipedia: {result[2]}")
    else:
        print("Ei tuloksia.")

def get_all_countries():
    sql = "SELECT iso_country, name, wikipedia_link FROM country;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall() # type of result: list
    #print("koko tuloslista:", result)
    print("tuloksia yhteensä:", cursor.rowcount)
    if cursor.rowcount > 0:
        for row in result:
            # type of row: tuple
            print(f"{row[0]}: {row[1]}, wikipedia: {row[2]}")
    else:
        print("Ei tuloksia.")

#get_country('SE')
#get_country('FI')
#get_country('asdf')

get_all_countries()

#unser_input = input("Anna koodi: ")
#get_country(unser_input)

"""
# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston avulla:

import mysql.connector
from geopy.distance import geodesic
from geopy.distance import great_circle
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


# Loading the lat-long data for Kolkata & Delhi
#icao_code1 = (22.5726, 88.3639)
#icao_code2 = (28.7041, 77.1025)

def get_icao_code1(icao_code1):
    sql = f"SELECT airport.latitude_deg,airport.longitude_deg FROM airport WHERE ident='{icao_code1}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result1 = cursor.fetchone()  # type of result: tuple

    if cursor.rowcount > 0:
        print(f"{result1[0]}, {result1[1]}")
        #print(geodesic(result1[0], result1[1]).km)
    else:
        print("Ei tuloksia.")

def get_icao_code2(icao_code2):
    sql = f"SELECT airport.latitude_deg,airport.longitude_deg FROM airport WHERE ident='{icao_code2}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result2 = cursor.fetchone()  # type of result: tuple

    if cursor.rowcount > 0:
        print(f"{result2[0]}, {result2[1]}")
        #print(geodesic(result2[0], result2[1]).km)
    else:
        print("Ei tuloksia.")

user_input1 = input("Anna ensimmäinen ICAO-koodi: ")
get_icao_code1(user_input1)

user_input2 = input("Anna toinen ICAO-koodi: ")
get_icao_code2(user_input2)
print("\n")

print(get_icao_code1(user_input1), 'hola1')
print(get_icao_code2(user_input2), 'hola2')

"""