
# Ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

sukupuoli = input("Anna biologinen sukupuoli kirjoittamalla (nainen / mies): ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo (g/l): "))

gender1 = "nainen"
gender2 = "mies"

if sukupuoli == gender1 and hemoglobiiniarvo < 117:
    print("Sinun hemoglobiiniarvo on alhainen.")
elif sukupuoli == gender1 and hemoglobiiniarvo <= 175:
    print("Sinun hemoglobiiniarvo on normaali.")
elif sukupuoli == gender1 and hemoglobiiniarvo > 175: # täällä voisikin olla 'else:'
    print("Sinun hemoglobiiniarvo on normaali korkea.")

if sukupuoli == gender2 and hemoglobiiniarvo < 134: # täällä voisikin olla 'elif:'
    print("Sinun hemoglobiiniarvo on alhainen.")
elif sukupuoli == gender2 and hemoglobiiniarvo <= 195:
    print("Sinun hemoglobiiniarvo on normaali.")
elif sukupuoli == gender2 and hemoglobiiniarvo > 195:
    print("Sinun hemoglobiiniarvo on normaali korkea.")

# else: print("Virheellinen syötö, yritä uudelleen..!")
