import random
from electric_car import ElectricCar
from combustion_car import CombustionCar

car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = CombustionCar("ACD-123", 165, 32.3)

cars = [car1, car2]

race_on = True
while race_on:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(3)
        if car.odo_meter >= 10000:
            race_on = False

print("__Tulokset__")
for car in cars:
    car.print_info()

