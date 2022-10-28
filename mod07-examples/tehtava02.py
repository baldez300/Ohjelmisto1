# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi
# tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
nimet.add(nimi)

while nimi != "":
    nimi = input("Anna toinen nimi tai lopeta painamalla Enter: ")
    nimet.add(nimi)
    if nimi == "":
        print(nimet)
        break

for p in nimet:
    print(p)