# niinkauan kuin maksettu rahamäärä < 5
# anna koliiko

hinta = int(input("Paljon maksaa?: "))
maksettu = 0
while maksettu < hinta:
    maksettu = maksettu + 1
    print("maksetaan 1 euro")
    #print("maksettavan jäljellä " + str(hinta - maksettu))
    print(f"maksettavan jäljellä {hinta - maksettu}")
print("Kahvi maksettu kokonaan")
#print(kommentti)

# ===============================================================================
# While esim. 2. " Ohjelmavalikko"
# niinkauan kuin maksettu rahamäärä < annettu hinta
# anna koliiko

command = ""
while command.lower() != "lopeta":
# Whilw True:
    command = input("Ana komento: ")
    # command = comand.lower()
    if command == "tulosta":
        print("tulostetaan")
    elif command == "help":
        print("komennot: tulosta, help, lopeta")
    elif command == "lopeta":
        print("ohjelma sammutetaan")
        # break # lopettaisi silmukan tähän testaamatta while-ehto uudestaan
    else:
        print("en ymmärrä, yritä uudestaan, kirjoita help saadeksesi apia")
print("ohjelma lopetettu")
#==============================================================================
import random
toistot = 0
heitot_yhteensä = 0
while toistot < 100000:

    noppa1 = noppa2 = heitot = 0
    while (noppa1!=6 or noppa2!=6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
        # print(f"Kierroksella {heitot}, noppa1: {noppa1}, noppa2: {noppa2}")
    print(f"Tarvittiin {heitot:d} heittoa.")
    toistot = toistot + 1
    heitot_yhteensä = heitot_yhteensä + heitot

heitot_keskimäärin = heitot_yhteensä/toistot
print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")