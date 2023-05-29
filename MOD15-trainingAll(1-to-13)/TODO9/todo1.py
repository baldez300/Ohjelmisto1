
# Write a Car class whose properties are license plate number, top speed, current speed, and distance traveled.
# Write an initializer in the class that sets the first two properties to the values received as parameters.
# The speed and distance traveled of the new car must be automatically set to zero.
# Write the main program to create a new car (registration code ABC-123, top speed 142 km/h).
# In the main program, print all the properties of the car created after that.

class Car:
    def __init__(self, reg_number, top_speed):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.speed = 0
        self.odometer = 0
        print("New car created")

    def print_info(self):
        print(f"Car {self.reg_number}, speed_limit {self.top_speed}, "
              f"Speed {self.speed}, distance traveled {self.odometer}")


car1 = Car("ABC-123", 120)
car1.print_info()
car2 = Car("DEF-69", 150)
car2.print_info()
car3 = Car("GHI", 180)
car3.print_info()