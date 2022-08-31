
# Only one (=) in python syötä operaattori
rahat = float(input("Anna rahamäärä: "))
if rahat >= 5:
    print("Voit ostaa latten.")
print("Kiitos kun testasit riittikö raha, moi!")
#========================================================
pituus = float(input("Kuinka pitkä olet: "))
if 1.5 <= pituus <= 2.0:
    print("Olet normali mittain.")

#========================================================
# Old school way
pituus = float(input("Kuinka pitkä olet: "))
if pituus >= 1.5 and pituus <= 2.0:
    print("Olet normali mittain.")

#========================================================
# Old school way
pituus = float(input("Kuinka pitkä olet: "))
if pituus < 1.5 or pituus > 2.0:
    print("Et olet normalimittainen.")

#========================================================
# Case sentive
mjono1 = input("Anna elälainlaji: ")
mjono2 = input("Anna elälainlaji: ")
if mjono1 == mjono2:
    print("Annoit sama eläinlaiji.")

#========================================================
# Case sentive
muutaja1 = 5
# Int-tyypinen, koska sinne sijoitettiin kokonaisluku 5

muutaja2 = 1.49
# Float-tyypinen, koska sinne sijoitettiin decimaaliluku 1.49

muutaja3 = "Rakas"
# String-tyypinen, koska sinne sijoitettiin string "Rakas"

muutaja4 = input("Kirjoitta numero:")
# String-tyypinen, jos halutaan vertaillla suuruutta tai laske

#==================================================================
ika = int(input("Anna ikäsi: "))
if ika >= 15 and ika < 18:
    paino = float(input("Anna painosi (kg): "))

if ika >= 18 or (ika >= 15 and paino >= 55):
    print("Lääken käyttö sallittu")

ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))
if (ikä >= 18 or ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")

#==================================================================
# Ei kaatu
ikä = int(input("Anna ikä: "))
if ikä >= ikä < 18:
    paino = float(input("Anna paino (kg): "))
if ikä < 18:
    print("Lääkkeen käyttö on sallittua.")
if ikä >= 15 and ikä < 18:
    if paino >= 55:
        print("Lääkkeen käyttö on sallittua.")

# ==========================================================
ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))
if (ikä >= 18 or ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")
else:
    print("Lääkettä ei saa käyttää.")

#============================================
ikä = int(input("Anna ikäsi: "))
if ikä >= 18:
    print("Lääkeen käyttö sallittu.")
elif ikä < 15:
    print("Lääkeen käyttö ei ole sallittu.")
else:
    paino = float(input("Anna painosi: "))
    if paino >= 55:
        print("Lääkeen käyttö sallittu.")
    else:
        print("Lääkeen käyttö ei ole sallittu.")
print("Kiitos kun käytit lääkeohjelmaa!")