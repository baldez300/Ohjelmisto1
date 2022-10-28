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


def get_two_icao_code2(icao_code1, icao_code2):
    sql = f"SELECT airport.latitude_deg,airport.longitude_deg FROM airport WHERE ident='{icao_code1}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result1 = cursor.fetchone()  # type of result: tuple
    print("Ensimmäinen sijainti (leveysaste, pituusaste): ", result1)

    sql2 = f"SELECT airport.latitude_deg,airport.longitude_deg FROM airport WHERE ident='{icao_code2}';"
    cursor = connection.cursor()
    cursor.execute(sql2)
    result2 = cursor.fetchone()  # type of result: tuple
    print("Toinen sijainti (leveysaste, pituusaste): ", result2)

    if (result1 == None) or (result2 == None):
        print("Ei tuloksia. Yritä uudelleen...")
    else:
        #print("\n")
        print('....')
        print("Laske kahden maan pisteen välinen etäisyys kahdella tavalla:")
        print("Niiden välinen etäisyys kilometreissä: ", geodesic(result1, result2).km, "km")
        print("Niiden välinen etäisyys kilometreissä: ", great_circle(result1, result2).km, "km")


user_input1 = input("Anna ensimmäinen ICAO-koodi: ")
user_input2 = input("Anna toinen ICAO-koodi: ")
get_two_icao_code2(user_input1, user_input2)
