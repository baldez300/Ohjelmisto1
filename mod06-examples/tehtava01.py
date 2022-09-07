# Funtions

"""def say_hello(name):
    # name on likaali muuttaja (arvo ei näy funtion ulkopoluolella)
    print(f"Moro {name}")
    print("Hyvää päivää!")
    return

# alla globaali name-muuttuja
name = "Aku"
say_hello("Iines")
say_hello("Minni Hiiri")
print(name)

def sum_of_two_ints(number1, number2):
    result = number1 + number2
    print(f"{number1} + {number2} = {result} hello")
    return result #paluuarvo

# funtiokutsu
result_sum = sum_of_two_ints(1, 2)
print("Summa: ", result_sum)
print("neljä + viisi =", sum_of_two_ints(4, 5)) """
# ========================================================

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
myRow = create_lottery_row(7, 39)
print("Lottorivi:", myRow)