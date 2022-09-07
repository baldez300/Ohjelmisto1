# Ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

"""list = []
while True:
    num = input("Anna numero: ")
    if num == "":
        break
    try:
        num = int(num)

        converted = int(num)
        list.append(converted)
        maximum = max(list)
        minimum = min(list)
    except:
        print("Väärä syöttö.")
        print("Yritä uudelleen..!")
        continue
    print("Maximum is", maximum)
    print("Minimum is", minimum)
print("Toiminnot lopetettu.")"""

# ====================SAME AS ABOVE =================
# Sinun kuvassa loituu se toinen ratkaisu voit sen tarkistaa
luku = []
while True:
    num = input("Anna numero: ")
    if num == "":
        break
    elif num:
        num = luku.append(int(num))
print(f"{min(luku)} pienin luku, {max(luku)} suurin luku")