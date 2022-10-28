import random
import time
# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.


class Auto:
    Cars = []

    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljetut_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = kuljetut_matka

    def kiihdyta(self, kmh):
        self.nopeus += kmh
        edennyt = 10000
        i = 1
        while i < edennyt:
            #print(i)
            i += kmh
        print(i)
        return

    def brake(self, kmh):

        if 0 <= kmh <= 20:
            self.nopeus -= kmh
            if self.nopeus < 10:
                print("This car has stopped")
                self.nopeus = 0
        else:
            print("Invalid braking value: {}".format(kmh))

    def kulje(self, numberofhours):
        time.sleep(numberofhours)
        return


Cars = []

auto1 = Auto("ABC-1", 110)
print(f"Rekisteritunnus: {auto1.rekisteritunnus}, Huippunopeus: {auto1.huippunopeus} km/h, "
      f"Nykyinen_nopeus: {auto1.nopeus} km/h, Kuljettu_matka: {auto1.matka} km\n")

auto1.kiihdyta(+15)
auto1.kulje(1)

for car in Cars:
    print(car)



