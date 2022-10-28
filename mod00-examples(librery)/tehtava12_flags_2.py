class Koira:
    jalka_maara = 4
    tehty = 0

    def __init__(self, nimi, syntymavuosi, rotu, paino, haukahdus="Vuh Vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.rotu = rotu
        self.paino = paino
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)


class Hoitola:
    def __init__(self):
        self.koirat = []

    def koiraSisaan(self, koira):
        self.koirat.append(koira)
        print(koira.nimi + ": Kirjattu sisään")

    def koiraUlos(self, koira):
        self.koirat.remove(koira)
        print(koira.nimi + ": Kirjattu ulos")

    def tervehdiKoiria(self):
        for piski in self.koirat:
            piski.hauku(2)


# PÄÄOHJELMA

koira1 = Koira("Churro", 1999, "Saksanpaimenkoira", 25, "Räyh Räyh")
# print(f"Koira1\nNimi: {koira1.nimi:s} \nSyntymävuosi: {koira1.syntymavuosi:d} \nRotu: {koira1.rotu:s} \nPaino: {koira1.paino:d} kg")
koira2 = Koira("Pulivari", 1938, "Berhandilainen", 40)
# print(f"Koira2\nNimi: {koira2.nimi} \nSyntymävuosi: {koira2.syntymavuosi} \nRotu: {koira2.rotu} \nPaino: {koira2.paino} kg")

koira1.hauku(5)
koira2.hauku(1)

print(Koira.jalka_maara)
print(koira1.jalka_maara)
Koira.jalka_maara = 3
print(koira2.jalka_maara)
print(f"Koiria on nyt {Koira.tehty}.")
koira1.tehty = 10
print(koira1.tehty, "\n") # Huom nyt vain koira1:den tyhty määrä kasvoi

hoitola = Hoitola()

hoitola.koiraSisaan(koira1)
hoitola.koiraSisaan(koira2)
hoitola.tervehdiKoiria()
hoitola.koiraUlos(koira2)