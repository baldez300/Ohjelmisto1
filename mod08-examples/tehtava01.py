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


def get_airport(icao_code):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao_code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    # haetaan vain yksi (=ensimmäinen) tulosrivi
    result = cursor.fetchone()  # type of result: tuple
    print("koko tulos monikko:", result)
    print("tuloksia yhteensä:", cursor.rowcount)
    if cursor.rowcount > 0:
        print(f"{result[0]}: {result[1]}")
    else:
        print("Ei tuloksia.")


unser_input = input("Anna ICAO-koodi: ")
get_airport(unser_input)