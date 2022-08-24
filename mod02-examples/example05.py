
# Ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

loaves = float(input("Anna leiviskät: "))
nails = float(input("Anna naulat: "))
bullets = float(input("Anna luodit: "))

# Conversin
grams = 13.3 * (bullets + (32 * (nails + (loaves * 20))))
if grams >= 1000:
    rounded_gram = round(grams, -3)

    grams = grams - rounded_gram
    rounded_gram = rounded_gram / 1000
print("Massa nykymittojen mukaan: ", end="")
print(str(round(rounded_gram)) + " kilogrammaa ja " + str(round(grams, 3)) + " grammaa.")