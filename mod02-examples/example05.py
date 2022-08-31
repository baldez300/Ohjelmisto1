
# Ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

loaves = float(input("Anna leiviskät: "))
nails = float(input("Anna naulat: "))
bullets = float(input("Anna luodit: "))

# Conversion
com_bullets = 13.3
com_nails = 32 * bullets
com_loaves = nails * 20

combined_bullets = com_bullets + float(loaves)
combined_nails = float(bullets)
combined_loaves = float(nails)

combined_weight = combined_bullets + combined_nails + combined_loaves
kilograms = combined_weight // 1000
grams = f"{(combined_weight / 1000 - kilograms) * 1000:.2f}"

print("Massa nykymittojen mukaan: ", end="")
print(f"{int(kilograms)} kilogrammaa ja  {grams:.2f}  grammaa.")

# Toinen tapa tehddä ==================================================
from math import floor
loaves = float(input("Anna leiviskät: "))
nails = float(input("Anna naulat: ")) + loaves * 20
bullets = float(input("Anna luodit: ")) + 32 * nails
grams = loaves * 13.3

kilo = floor(grams / 1000)
print("Massa nykymittojen mukaan: ", end="")
print(f"{kilo} kilogrammaa ja {grams % 1000:.2f} grammaa.")
