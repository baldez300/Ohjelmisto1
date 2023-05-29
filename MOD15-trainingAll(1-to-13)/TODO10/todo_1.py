# Write an Elevator class that receives the lowest and highest floor number as its initializer parameters.
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
    def __init__(self, topfloor, bottomfloor=1):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.currentfloorn = bottomfloor

    def floorup(self):
        self.currentfloorn += 1
        print(f"elevator moved up to {self.currentfloorn}")

    def floordown(self):
        self.currentfloorn -= 1
        print(f"elevator moved down to {self.currentfloorn}")

    def movetofloor(self, floormoveto):
        if self.bottomfloor > floormoveto or self.topfloor < floormoveto:
            print("no such floor.")
            return
        floorreached = False
        while not floorreached:
            if floormoveto == self.currentfloorn:
                print("u have reached ur desired floor")
                floorreached = True
            elif floormoveto > self.currentfloorn:
                print(f"elevator movıng up to {self.currentfloorn + 1}")
                self.floorup()
            elif floormoveto < self.currentfloorn:
                print(f"elevator movıng down to {self.currentfloorn - 1}")
                self.floordown()
            # else:


Elevator(10)


class House:
    def __init__(self, highestfloor, lowestfloor, num_of_el):
        self.listofele = []
        for i in range(num_of_el):
            self.listofele.append(Elevator(highestfloor, lowestfloor))

    def firealarm(self):
        for elevator in self.listofele:
            elevator.movetofloor(elevator.bottomfloor)

    def rideele(self, eleid, floor):
        self.listofele[eleid - 1].movetofloor(floor)


house1 = House(25, -5, 150)
house1.rideele(150, 24)
house1.firealarm()
