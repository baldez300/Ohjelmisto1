# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

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


def get_countries_code(iso_code):
    #sql = f"SELECT country.iso_country, country.name, airport.name, type FROM country, airport WHERE country.iso_country='{iso_code}'AND airport.iso_country='{iso_code}';"
    sql = f"SELECT type, count(*) as 1km FROM airport WHERE iso_country='{iso_code}' GROUP BY type;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()  # type of result: list
    #print("koko tuloslista:", result)
    print("tuloksia yhteensä:", cursor.rowcount)
    if cursor.rowcount > 0:
        for row in result:
            # type of row: tuple
            #print(f"{row[0]}: {row[1]}, airport name: {row[2]}, airport type: {row[3]}")
            print(f"{row[0]}: {row[1]}")
    else:
        print("Ei tuloksia.")


unser_input = input("Anna koodi: ")
get_countries_code(unser_input)