# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

start = int(input("Enter start number: "))
end = int(input("Enter last number: "))

while start <= end:
    if start % 3 == 0:
        print(start)
    start += 1


