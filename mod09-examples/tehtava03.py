# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

    def drive(self, hours):
        self.odometer += self.speed * hours

    def prin_info(self):
        print(f"Auton {self.reg_number}, huippunopeus {self.top_speed} km/h, "
              f"Nopeus {self.speed}, kuljettu matka {self.odometer} km")


car1 = Car("ABC-123", 230)
car1.accelerate(30)
car1.drive(1)
car1.prin_info()
car1.accelerate(70)
car1.drive(0.5)

car1.accelerate(-200)
car1.prin_info()
