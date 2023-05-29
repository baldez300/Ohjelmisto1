# The mission is a continuation of the previous car racing mission.
# Write a Race class that has the name of the race,
# the length in kilometers and the list of participating cars as properties.
# The class has an initializer that receives as parameters name, mileage and car list and
# sets them as values for properties. The class has the following methods:
#
# tunti_kuluu, which implements the hourly actions mentioned in the previous car racing task
# i.e. draws the speed change of each car and calls the go method for each car.
# print_status, which prints the current information of all cars in a clear table format.
# race_over which returns True,
# if one of the cars is at the finish line, i.e. it has driven at least the total number of kilometers of the race.
# Write a main program that creates an 8000 km race called "The Great Scrap Rally".
# The race to be created is given a list of ten cars in the same way as in the previous task.
# The main program simulates the progress of the race by calling the run hour method in the repetition structure,
# after which we always check whether the race is over using the race_over method.
# The up-to-date situation is printed using the situation method every ten hours and once after that,
# when the race is over.

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

