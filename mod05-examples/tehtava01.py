# Ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.

import random
# "lottokone" arpoo n numero välillä 1-total_numbers
def create_lottery_row(numberAmount, total_number):
    row = []
    for i in range(numberAmount):
        rndNum = random.randint(1, total_number)
        while row.count(rndNum) > 0:
            print("tuli tupla:", rndNum)
            rndNum = random.randint(1, total_number)
        row.append(rndNum)
        print(f"{i+1}. nro: {rndNum}")
    row.sort()
    return row

# Pääohjelma = (funktion ulkopuolella)
lottery_number = int(input("Anna arpakuutioiden lukumäärä (7): "))

myRow = create_lottery_row(lottery_number, 39)
print("Lottorivi:", myRow)