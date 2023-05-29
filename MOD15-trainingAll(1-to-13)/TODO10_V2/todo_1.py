# Write an Elevator class that receives
# the lowest and highest floor number as its initializer parameters.
# The elevator has methods move_to_floor, floor_up and floor_down.
# The new elevator is always on the lowest floor.
# If, for example, you make a method call to the created elevator h.go to_floor(5),
# the method calls either the layer_up or layer_down method as many times as
# that the elevator ends at the fifth floor.
# The latter methods drive the elevator up or down one floor and declare,
# which floor is the elevator after that.
# Test the class by creating an elevator in the main program and telling it to move to the floor you want
# and after that back to the bottom layer.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor

    def move_to_floor(self, floor):
        if self.bottom_floor <= floor <= self.top_floor:
            while self.floor < floor:
                self.up_floor()
            while self.floor > floor:
                self.down_floor()
        else:
            print("The floor in question does not exist")

    def up_floor(self):
        if self.floor < self.top_floor:
            self.floor += 1
            print(f"On the floor {self.floor}")

    def down_floor(self):
        if self.floor > self.bottom_floor:
            self.floor -= 1
            print(f"On the floor {self.floor}")


e = Elevator(1, 5)
e.move_to_floor(3)
e.move_to_floor(1)
e.move_to_floor(5)
e.move_to_floor(100)
e.move_to_floor(1)
