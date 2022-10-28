# Count visited countries flags

from collections import Counter
import mysql.connector
import flag


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

flag_input = input("Anna iso_country code: ")
sql = f"SELECT iso_country FROM country WHERE iso_country = '{flag_input}';"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchone()  # type of result: list

while not result:
    print("Error input. Try again...")
    flag_input = input("Anna iso_country code: ")
    sql = f"SELECT iso_country FROM country WHERE iso_country = '{flag_input}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()  # type of result: list

flag_list = []
for code in result:
    flag = flag.flag(code)
    flag_list = {code: flag}
print(flag_list)


"""
def connect_dat():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user',
        password='password',
        autocommit=True
        )


connetion = connect_dat()


def collected_flags(id_value):
    sql = f"UPDATE game SET (tickets_amount = '{id_value}' )"
    cursor = connetion.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        print(i[0])

    if not result:
        print("Wrong entry, try gain..")
    else:
        return result


flag_list = []
count_flag = 0

while count_flag < 10:
    flag = input("Anna lipun omistavan maan nimi: ")
    flag_list.append(flag)
    count_flag += 1
    print(Counter(flag_list))
    collected_flags(flag_list) """



"""import flag

flag = flag.flag("IL")
'🇮🇱'
print(flag)

 flag.flag("GBENG")
'🏴󠁧󠁢󠁥󠁮󠁧󠁿'

flag.flagize("Flag of Israel :IL:")
'Flag of Israel 🇮🇱'

flag.dflagize("Flag of Israel 🇮🇱")
'Flag of Israel :IL:'

flag.flagize("England :gb-eng: is part of the UK :GB:", subregions=True)
'England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧'

flag.dflagize("England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧", subregions=True)
'England :gb-eng: is part of the UK :GB:'
"""