
# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljetut_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = kuljetut_matka

    def kiihdytä(self, kmh):
        self.nopeus += kmh
        if 0 < self.nopeus <= self.huippunopeus:
            print(f"Auto kiihtyy: {self.nopeus} km/h")
        elif self.nopeus >= self.huippunopeus:
            print(f"Auto on saavuttanut huippunopeutensa: {self.huippunopeus} km/h")
        elif kmh == -200:
            self.nopeus = 0
            print(f"Olet painanut hätäjarrua: {self.nopeus} km/h")
        return


auto1 = Auto("ABC-123", 142)
print(f"Uuden auton rekisteritunnus: {auto1.rekisteritunnus} "
      f"\n Sen huippunopeus: {auto1.huippunopeus} km/h")

auto1.kiihdytä(+30)
auto1.kiihdytä(+70)
auto1.kiihdytä(+50)
auto1.kiihdytä(-200)