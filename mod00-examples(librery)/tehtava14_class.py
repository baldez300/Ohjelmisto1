class Auto:
    def __init__(self, rekkari, vari):
        self.rekkari = rekkari
        self.vari = vari


class Maalaamo:
    def maalaa(self, auto, vari):
        auto.vari = vari


kotsa = Auto("ABC-123", "ruskea")
print(kotsa.vari)
penanMaalaamo = Maalaamo()
penanMaalaamo.maalaa(kotsa, "punainen")
print(kotsa.vari)