# Now programming a car race. The distance traveled by the new car is automatically initialized to zero.
# At the beginning of the main program,
# make a list consisting of ten auto-objects created with the repetition structure.
# The top speed of each car is drawn between 100 km/h and 200 km/h.
# The registration ID is generated as follows "ABC-1", "ABC-2", etc. Then the competition begins.
# During the competition, the following measures are taken every hour:
#
# The speed of each car is changed so that the speed change is drawn between -10 and +15 km/h.
# This is done by calling the accelerate method.
# All cars are told to move for one hour. This is done by calling the go method.
# The competition continues until one of the cars has traveled at least 10,000 kilometers.
# Finally, all the characteristics of each car are printed in a clear table.
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

    def print_info(self):
        print(f"Car {self.reg_number}, top speed {self.top_speed} km/h, "
              f"Speed {self.speed}, distance traveled {self.odometer} km")


cars = []

for i in range(10):
    new_car = Car(f"ABC-{i + 1}", random.randint(100, 200))
    # new_car.prin_info()
    cars.append(new_car)

race_on = True
while race_on:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        # car.prin_info()
        if car.odometer >= 10000:
            race_on = False
print("__Results__")
for car in cars:
    car.print_info()
