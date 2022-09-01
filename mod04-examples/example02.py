# Ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.

inch_value = int(input('Enter the value in inch: '))

while inch_value != 0:
    cm_value = 2.54 * inch_value
    if inch_value < 0:
       print("Negative entry, try again with positive numbers.")
       break
    print('{}″ = {}cm'.format(inch_value, cm_value))
    break