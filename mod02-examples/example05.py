
# Ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

loaf = float(input("Anna leiviskät: "))
nail = float(input("Anna naulat: "))
bullet = float(input("Anna luodit: "))
# print("Your body mass index is: ", round(weight / (height * height), 2))
# Conversin
grams = 13.3 * (bullet + (32 * (nail + (loaf * 20))))
if grams >= 999:
    rounded_gram = round(grams, -3)

    grams = grams - rounded_gram
    rounded_gram = rounded_gram / 1000
print("Massa nykymittojen mukaan: ", end="")
print(str(round(rounded_gram)) + " kilogrammaa ja " + str(round(grams, 3)) + " grammaa.")