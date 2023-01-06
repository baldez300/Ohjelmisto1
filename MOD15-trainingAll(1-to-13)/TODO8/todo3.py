
# Write a program that prompts the user for the ICAO codes of two airports.
# The program indicates the distance between the airports in kilometers.
# The calculation is based on the coordinates retrieved from the database.
# Calculate the distance using the geopy library:
# "https://geopy.readthedocs.io/en/stable/ ".
# Select View / Tool Windows / Python Packages to install the library.
# Enter geopy in the search field and complete the installation.

import mysql.connector
from geopy import distance


connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user',
        password='password',
        autocommit=True
    )


def distance_between_airports(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao.upper()}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchone()


a_location = distance_between_airports(input("Give airport ICAO-code: "))
b_location = distance_between_airports(input("Give airport ICAO-code: "))

distance_in_km = distance.distance(a_location, b_location).miles * 1.609344
print(f"The distance between the airports is: {distance_in_km:.2f} km")
