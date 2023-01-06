
# Write a program that asks the user for the country code (for example FI)
# and prints the number of airports in that country by type.
# For example, for Finland, the result must be information that there are 65 small airports, 15 heliports, etc.

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


def country_airports_types(country):
    sql = f"SELECT type FROM airport WHERE iso_country='{country.upper()}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


results = country_airports_types(input("Give country code name: "))
airport_size_count = {}
for result in results:
    if result in airport_size_count:
        airport_size_count[result] += 1
    else:
        airport_size_count[result] = 1

for key, value in airport_size_count.items():
    print(f"\nAirport Type: {key[0]} is {value} pcs")

















