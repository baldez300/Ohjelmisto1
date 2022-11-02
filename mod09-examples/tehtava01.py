# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
# jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, reg_number, top_speed):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.speed = 0
        self.odometer = 0
        print("Uusi auto luottu")

    def prin_info(self):
        print(f"Auton {self.reg_number}, huippunopeus {self.top_speed}, "
              f"Nopeus {self.speed}, kuljettu matka {self.odometer}")


car1 = Car("ABC-123", 120)
car1.prin_info()
car2 = Car("ABC-69", 150)
car2.prin_info()
#car3 = Car()
