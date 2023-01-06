
# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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
        else: print("The floor in question does not exist")

    def up_floor(self):
        if self.floor < self.top_floor:
            self.floor += 1
            print(f"On the floor {self.floor}")

    def down_floor(self):
        if self.floor > self.bottom_floor:
            self.floor -= 1
            print(f"On the floor {self.floor}")


class House:
    def __init__(self, bottom_floor, top_floor, elevator_lkm):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(elevator_lkm)]

    def ride_the_elevator(self, elevator, floor):
        if elevator <= len(self.elevators):
            print(f"The elevator {elevator} is activating")
            self.elevators[elevator-1].move_to_floor(floor)
        else: print("The elevator does not exist")


h = House(1, 5, 2)
h.ride_the_elevator(1, 3)
h.ride_the_elevator(2, 5)
h.ride_the_elevator(2, 100)
h.ride_the_elevator(2, 1)
h.ride_the_elevator(10, 1)
h.ride_the_elevator(1, 1)