# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

# Calculating pizza price efficiency in Python (for the selected coding down below in green)
"""import math


def price_per_squinch(diameter, price):
    rad = diameter / 2.0
    area = math.pi * rad ** 2
    return price / area


def price_per_squinch_crusthater(diameter, price, crustwidth=1):
    #Return the price per square inch of a pizza with the given diameter and
    #price, excluding the crust with width specified.

    delicious_diam = min(0, diameter - (crustwidth * 2))
    return price_per_squinch(delicious_diam, price)


def prompt_bool(prompt_text):
    while 1:
        inp = input(prompt_text)
        if inp in 'yYnN':
            return inp in 'yY'
        else:
            print
            'Choose Y or N please.'


def prompt_float(prompt_text):
    while 1:
        inp = input(prompt_text)
        try:
            return float(inp)
        except ValueError:
            print
            'Please enter a number with no symbols other than digits and a decimal point.'


def main():
    print
    "Welcome to the Python Pizza Price Pcalculator"
    likes_crusts = prompt_bool("Do you like crusts? (Y/N) ")
    price_fn = price_per_squinch if likes_crusts else price_per_squinch_crusthater
    while 1:
        diam = prompt_float("What is the diameter of the pizza?: ")
        price = prompt_float("What is the price of the pizza in EURO?: ")

        try:
            ppsq = price_fn(diam, price)
        except ZeroDivisionError:
            print("Price per square inch is undefined. Your pizza is either 0-dimensional, or you don't like crusts and it's completely crusty.")
            continue
        print("The price per square inch is %.2f" % ppsq)
        break

        #print("Let's calculate the cost of another pizza!")


if __name__ == '__main__':
    main()"""

# Toinen vaihtoehto ===============================================
import math
meemit = ["ovat", "tärkeitä"]
count = 0
i = 0


def pizzahinta(fdiameter, fprice):
    return fprice / (math.pi * fdiameter)


while count < 2:
    try:
        price = float(input(f"Anna {i+1} pizzan hinta: "))
        diameter = float(input(f"Anna {i+1} pizzan halkaisija: "))
        priceperarea = pizzahinta(diameter, price)
    except ValueError:
        print("Syötä numero!")
    else:
        print(f"Pizzan hinta per neliömetri on {round(pizzahinta(diameter, price), 2)}€.")
        if i == 0:
            price1 = round(priceperarea, 2)
            i += 1
        elif i == 1:
            price2 = round(priceperarea, 2)
        count += 1

if price1 == price2:
    print("Molemilla pizzoilla on sama hinta per bite.")
elif price1 < price2:
    print("Ekalla pizzalla on parempi hinta.")
else:
    print("Toisella pizzalla on parempi hinta.")
