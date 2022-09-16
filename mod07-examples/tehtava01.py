# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

kuukauden_numero = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
kuukausi = kuukauden_numero[järjestysnumero - 1]

if järjestysnumero == 12 or järjestysnumero == 1 or järjestysnumero == 2:
    print("talvi")
elif järjestysnumero == 3 or järjestysnumero == 4 or järjestysnumero == 5:
    print("kevät")
elif järjestysnumero == 6 or järjestysnumero == 7 or järjestysnumero == 8:
    print("kesä")
elif järjestysnumero == 9 or järjestysnumero == 10 or järjestysnumero == 11:
    print("syksy")
else:
    print("Invalid Month Number")

print('\n')
print(f"{järjestysnumero}. kuukausi on {kuukausi}.")

