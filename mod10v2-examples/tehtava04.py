
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
        self.odometer = 0  # matka

    def accelerate(self, delta_speed):
        self.speed += delta_speed
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.odometer += round(self.speed * hours)


class Race:
    def __init__(self, name, lenght, car_amount):
        self.name = name
        self.lenght = lenght
        self.carlist = []
        for i in range(car_amount):
            trucker = "ABC-" + str(i+1)
            speed_limit = random.randint(100, 200)
            self.carlist.append(Car(trucker, speed_limit))

    def hour_passed(self):
        for car in self.carlist:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_standings(self):
        print(f'{"Registration number":<20} {"Top speed":<15} {"Speed":<10} {"Odometer":<20}')
        for car in self.carlist:
            max_speed = f"{car.top_speed} km/h"
            speed = f"{car.speed} km/h"
            odometer = f"{car.odometer} km"
            print(f"{car.reg_number:<20} {max_speed:<15} {speed:<10} {odometer:<20}")

    def is_race_over(self, ):
        for car in self.carlist:
            if car.odometer >= self.lenght:
                return True
        return False


race = Race("The big scrap rally", 8000, 10)

while not race.is_race_over():
    race.hour_passed()
race.print_standings()

