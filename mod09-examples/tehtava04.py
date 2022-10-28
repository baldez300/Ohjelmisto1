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
    edennyt = []
    while edennyt > 10:
        edennyt.append()
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljetut_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = kuljetut_matka

    def kiihdytä(self, kmh):
        self.nopeus += kmh
        return

    def kulje(self, numberofhours):
        edennyt = 10000
        self.nopeus = 1
        return


auto1 = Auto("ABC-1")
print(f"Uuden auton rekisteritunnus: {auto1.rekisteritunnus} \n")

auto1.kiihdytä(-10)
auto1.kiihdytä(+15)
auto1.kulje(1.5)

print("\n")

auto2 = Auto("ABC-2")
print(f"Uuden auton rekisteritunnus: {auto2.rekisteritunnus} \n")

auto2.kiihdytä(-10)
auto2.kiihdytä(+15)
auto2.kulje(1.5)