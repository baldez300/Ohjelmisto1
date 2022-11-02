from car_race import Car


class ElectricCar(Car):
    def __init__(self, reg_number, top_speed, capacity):
        super().__init__(reg_number, top_speed)
        self.capacity = capacity

    def print_info(self):
        super().print_info()
        print(f"The car capacity is: {self.capacity}-kWh.\n")