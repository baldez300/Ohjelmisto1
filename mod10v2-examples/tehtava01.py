
# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
# ja sen jälkeen takaisin alimpaan kerrokseen.

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


e = Elevator(1, 5)
e.move_to_floor(3)
e.move_to_floor(1)
e.move_to_floor(5)
e.move_to_floor(100)
e.move_to_floor(1)