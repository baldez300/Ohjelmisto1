
# Ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi tai ei.

vuosiluku = int(input("Anna vuosiluku: "))
if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
    print("Annettu vuosi on karkausvuosi.")
else:
    print("Annettu vuosi ei ole karkausvuosi!")
    print("Yritä uudelleen..!")