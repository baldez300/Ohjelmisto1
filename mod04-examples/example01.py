# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

start = int(input("Enter start number(1): "))
end = int(input("Enter last number(1000): "))

while start <= end:
    if start % 3 == 0:
        print(start)
    start += 1


