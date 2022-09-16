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

#get_all_countries()

unser_input = input("Anna koodi: ")
get_country(unser_input)