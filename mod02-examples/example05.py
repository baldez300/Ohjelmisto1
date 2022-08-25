
# Ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

loaves = float(input("Anna leiviskät: "))
nails = float(input("Anna naulat: "))
bullets = float(input("Anna luodit: "))

# Conversion

combined_bullets = 13.3 * bullets
combined_nails = 32 * nails
combined_loaves = (loaves * 20) // 2

combined_weight = combined_bullets + combined_nails + combined_loaves
kilograms = combined_weight // 1000
grams = f"{(combined_weight / 1000 - kilograms) * 1000:.2f}"

print("Massa nykymittojen mukaan: ", end="")
print(str(kilograms+combined_loaves) + " kilogrammaa ja " + str(grams) + " grammaa.")