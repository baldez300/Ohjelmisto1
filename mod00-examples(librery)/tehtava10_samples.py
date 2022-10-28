"""
players = []
playerscount = 0

while playerscount < 2:
    player = input("Anna peleyan nimi: ")
    players.append(player)
    playerscount += 1
print(players)
# ===============================================
maa1 = []
maa2 = ["Suomi", "Ruotsi", "Norja"]
maa3 = ["Viro", "Latvia"]
maa2.extend(maa3)  # extend() lisää koko lista toiseen
maa1.extend(maa2)
maa1.append("Puola")

print(maa1[1])
if "Viro" in maa2:
    print("Juu")
else:
    print("Ei")
if "Viro" in maa1:
    print("Joopajoo")
else:
    print("Eipäei")
print(maa1[-1])
# ===============================================
luku = range(0, 10, 2)
for i in luku:
    print(i)

# ===============================================
def suorakulmion_piiri(sivu1, sivu2):
    piiri = (sivu1 + sivu2) * 2

    return piiri


sivu1 = 7
sivu2 = 3
print(f"Suorakulmion sivut ovat {sivu1} ja {sivu2}")
print(f"Suorakulmion piiri on {suorakulmion_piiri(sivu1, sivu2)}")


def parittomat(luvutlista):
    print(luvutlista)
    pl = []
    for x in luvutlista:
        if x % 2 != 0:
            pl.append(x)
    return pl


luvut = [12, 2, 6, 7, 9, 5, 21, 4, 8, 10, 11]
parittomat = parittomat(luvut)
print("Alkuperäiset luvut: " + str(luvut))
print("parittomat luvut: " + str(parittomat))

s = "J"
while s != "Jeeee":
    print(s)
    s += "e"

nnbbnn"""

# Toinen osa koe alkaa tasta =====================================
i = 1
while i % 5 > 0:
    print(i)
    i += 3
print(i)

print("\n")
# =================
people = ("Mary", "Ahmed", "Pekka", "Olga")
olga, pekka, ahmed, mary = people
print(ahmed)
print(people[3])
if "Tiina" not in people:
    print(people)

# =================


def bytes_to_megabytes(bytes2):
    # bytes = 748723979
    kilobyte_1 = bytes2 * 1024
    megabytes2 = kilobyte_1 * 1024
    return megabytes2


bytes_1 = 748723979
megabytes = bytes_to_megabytes(bytes_1)
print(f"{bytes_1:d} B = {megabytes:.2f} MB")