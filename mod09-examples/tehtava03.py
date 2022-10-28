# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljetut_matka=2000):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = kuljetut_matka

    def kiihdytä(self, kmh):
        self.nopeus += kmh
        if 0 < self.nopeus <= self.huippunopeus:
            print(f"Auto kiihtyy: {self.nopeus} km/h ")
        elif self.nopeus >= self.huippunopeus:
            print(f"Auto on saavuttanut huippunopeutensa: {self.huippunopeus} km/h")
        elif kmh == -200:
            self.nopeus = 0
            print(f"Olet painanut hätäjarrua: {self.nopeus} km/h")
        return

    def kulje(self, numberofhours):
        if self.nopeus == 60:
            self.matka += self.nopeus * numberofhours
            print(f"\nKuljetut matka on: {self.matka} km")
        return


auto1 = Auto("ABC-123", 142)
print(f"Uuden auton rekisteritunnus: {auto1.rekisteritunnus} "
      f"\n Sen huippunopeus: {auto1.huippunopeus} km/h")

auto1.kiihdytä(+30)
auto1.kiihdytä(+20)
auto1.kiihdytä(+10)

auto1.kulje(1.5)