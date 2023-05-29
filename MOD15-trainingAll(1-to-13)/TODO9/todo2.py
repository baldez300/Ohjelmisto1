# Continue the program by writing the accelerate method in the Auto class,
# which receives the speed change (km/h) as a parameter.
# If the change in speed is negative, the car slows down.
# The method must change the value of the car object's speed property.
# The car's speed must not increase above the top speed or decrease below zero.
# Continue the main program so that the car's speed is first increased +30 km/h, then +70 km/h and finally +50 km/h.
# After this, print the speed of the car.
# Then perform emergency braking by specifying a speed change of -200 km/h and print the new speed.
# The traveled distance does not need to be updated yet.

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

    def print_info(self):
        print(f"Car's {self.reg_number}, top speed {self.top_speed}, "
              f"Speed {self.speed}, distance traveled {self.odometer}")


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
