# The mission is a continuation of the previous car racing mission.
# Write a Race class that has the name of the race, the length in kilometers and the list of participating cars as properties.
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
        self.odometer = 0
        # print("New car created")

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
        print(f"{self.reg_number}, top speed {self.top_speed} km/h, "
              f"Speed {self.speed}, distance traveled {self.odometer} km")


class Race:
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars
        self.hours_passed = 0

    def hour_passed(self):
        self.hours_passed = self.hours_passed + 1
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def is_race_over(self, ):
        for car in self.cars:
            if car.odometer > self.length:
                return True

    def print_standings(self):
        self.cars.sort(key=self.sort_cars, reverse=True)
        print(f"Competition {self.name} results after driving {self.hours_passed} hours")
        for car in self.cars:
            car.prin_info()

    def sort_cars(self, car):
        return car.odometer


cars = []

for i in range(10):
    new_car = Car(f"ABC-{i + 1}", random.randint(100, 200))
    cars.append(new_car)

myRace = Race("Big Scrap Rally", 800, cars)

race_on = True
while race_on:
    myRace.hour_passed()
    race_on = not myRace.is_race_over()
    if myRace.hours_passed % 10 == 0:
        myRace.print_standings()
print("Final Results")
myRace.print_standings()
