# Ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen.

luvut = []

luku = input("Anna ensimmäinen luku tai lopeta painamalla Enter: ")
while luku != "":
    luvut.append(luku)
    luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")

for n in luvut:
    print(f"{n}")

luvut.sort(reverse=True)
print(f"Viisi suurinta suuruusjärjestyksessä suurimmasta alkaen: {luvut[:5]}" )
