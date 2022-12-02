
# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Car:
    def __init__(self, reg_number, top_speed):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.speed = 0
        self.odometer = 0
        print("Uusi auto luottu")

    def accelerate(self, delta_speed):
        if self.top_speed >= delta_speed + self.speed > 0:
            self.speed = self.speed + delta_speed
        elif delta_speed + self.speed > self.top_speed:
            self.speed = self.top_speed
        else:
            self.speed = 0

    def print_info(self):
        print(f"Auton {self.reg_number}, huippunopeus {self.top_speed}, "
              f"Nopeus {self.speed}, kuljettu matka {self.odometer}")


car1 = Car("ABC-123", 130)
# car1.prin_info()
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.print_info()
car1.accelerate(-200)
car1.print_info()

# car2 = Car("ABC-69", 150)
# car2.prin_info()
# car3 = Car()