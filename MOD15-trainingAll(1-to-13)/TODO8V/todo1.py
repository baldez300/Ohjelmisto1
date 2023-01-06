
# Only for training purposes

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='user',
    password='password',
    autocommit=True
)


def get_country():
    sql = """SELECT * FROM country"""
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        print(result)


get_country()