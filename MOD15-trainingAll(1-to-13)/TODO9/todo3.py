# Expand the program so that there is a go method that takes the number of hours as a parameter.
# The method increases the traveled distance as much as the car has moved at a constant speed in the given number of hours.
# Example: the current traveled distance of the car is 2000 km. The speed is 60 km/h.
# Method call auto.kulje(1.5) increases the traveled distance to 2090 km.

class Car:
    def __init__(self, reg_number, top_speed):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.speed = 0
        self.odometer = 0
        print("New car created")

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


car1 = Car("ABC-123", 230)
car1.accelerate(30)
car1.drive(1)
car1.print_info()

car1.accelerate(70)
car1.drive(0.5)
car1.print_info()

car1.accelerate(-200)
car1.print_info()
