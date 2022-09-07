
# Ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# ja tulostaa sen sanallisen kuvauksen.

# This line below is for upper and lower case (esim. "lux" .upper -> "LUX")
# hyttiluokka = hyttiluokka.upper()

hyttiluokka = input("Anna laivan hyttiluokan merkki? (LUX, A, B, C): ")
if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka!")
    print("Yritä uudelleen..!")
