
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
        if  self.bottomfloor > floormoveto or self.topfloor < floormoveto:
            print("no such floor.")
            return
        floorreached = False
        while not floorreached:
            if floormoveto == self.currentfloorn:
                print("u have reached ur desıred floor")
                floorreached = True
            elif floormoveto > self.currentfloorn:
                print(f"elevator movıng up to {self.currentfloorn + 1}")
                self.floorup()
            elif floormoveto < self.currentfloorn:
                print(f"elevator movıng down to {self.currentfloorn - 1}")
                self.floordown()
            #else:
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
house1.rideele(150,24)
house1.firealarm()