# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja
# asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
#
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True,
# jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa aja tunti-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
# kun kilpailu on päättynyt.
import random


class Car:
    def __init__(self, reg_number, top_speed):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.speed = 0
        self.odometer = 0
        # print("Uusi auto luottu")

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
        print(f"{self.reg_number}, huippunopeus {self.top_speed} km/h, "
              f"Nopeus {self.speed}, kuljettu matka {self.odometer} km")


class Race:
    def __init__(self, name, lenght, cars):
        self.name = name
        self.lenght = lenght
        self.cars = cars
        self.hours_passed = 0

    def hour_passed(self):
        self.hours_passed = self.hours_passed +1
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def is_race_over(self, ):
        for car in self.cars:
            if car.odometer > self.lenght:
                return True

    def print_standings(self):
        self.cars.sort(key=self.sort_cars, reverse=True)
        print(f"KIlpailu {self.name} tulokset, kun ajettu {self.hours_passed} tuntia")
        for car in self.cars:
            car.prin_info()

    def sort_cars(self, car):
        return car.odometer


cars = []

for i in range(10):
    new_car = Car(f"ABC-{i + 1}", random.randint(100, 200))
    cars.append(new_car)

myRace = Race("Suuri romuralli", 800, cars)

race_on = True
while race_on:
    myRace.hour_passed()
    race_on = not myRace.is_race_over()
    if myRace.hours_passed % 10 == 0:
        myRace.print_standings()
print("Lopulliset tulokset")
myRace.print_standings()


