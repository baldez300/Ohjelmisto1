
# Write a program that prompts the user for the airport's ICAO code.
# The program searches for and prints the name of the airport corresponding to the code
# and its location from the airport database used in the course.
# The ICAO code is stored in the ident column of the airport table.

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

sql = "SELECT name, municipality FROM airport WHERE ident='EFHK';"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchone()
print("Total result plural:", result, "\n")
print("Output together:", cursor.rowcount, "\n")
print(f"Airport name: {result[0]}\nAirport location: {result[1]}\n")


# Same as above using function by using 'fetchone()' method
def airport(icao):
    sql2 = f"SELECT name, municipality FROM airport WHERE ident='{icao}';"
    cursor2 = connection.cursor()
    cursor2.execute(sql2)
    result2 = cursor2.fetchone()
    if cursor2.rowcount > 0:
        print(f"Airport name: {result2[0]}\nAirport location: {result2[1]}\n")
    else:
        print("Airport not found..")


icao_code = input("Enter the ICAO-code: ").upper()
airport(icao_code)


# Same as above using second function by using 'fetchall()' method
def search_icao(icao):
    sql3 = f"""SELECT name, municipality FROM airport WHERE ident="{icao.upper()}";"""
    cursor3 = connection.cursor()
    cursor3.execute(sql3)
    return cursor3.fetchall()


results = search_icao(input("Give an icao-code: "))
for result in results:
    print(f"""Name: {result[0]}, located in the municipality: {result[1]}.""")