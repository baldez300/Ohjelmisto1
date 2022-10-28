# Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä ja
# toteuttaa piin likiarvon laskennan edellä kuvatulla menetelmällä.
# Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle.
# (Huomaa, että jokaisesta arvotusta pisteestä (x,y) on helppoa testata
# onko se yksikköympyrän A sisällä: riittää testata, toteuttaako piste epäyhtälön x^2+y^2<1.)
import random

ind = 0
number_of_entries = 0  # N
inside_of_cercle = 0  # n
# Number of coordinates generated
number_of_entries = int(input("Montakohan pistettä generoidaan?: "))

# Evaluating positions
while ind < number_of_entries:
    xcor = random.uniform(-1, 1)
    ycor = random.uniform(-1, 1)
    if (xcor ** 2) + (ycor ** 2) < 1:
        inside_of_cercle += 1
    ind += 1

# Calculating pi(3,14)
print(4 * inside_of_cercle / number_of_entries)