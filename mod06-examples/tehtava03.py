# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
# joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
import random
def main(gallons):

    while gallons > 0:
        liters = float(gallons * 3.78)
        print("There are " + str(format(liters,'5.2f')) + " Liter(s) in " + str(gallons) + " Gallon(s), balde")
        gallons = float(input("Anna toinen gallonan arvo: "))

        if gallons < 0:
            print("Error entry.")
            break
    print("Wrong, negative or zero entry.")


gallons_amount = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoina: "))
main(gallons_amount)

