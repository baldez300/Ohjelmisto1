# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
number = random.randint(1, 10)
attempts = 0
guess = 0

while guess != number:
    guess = eval(input("Guess a number: "))
    attempts += 1

    if guess == number:
        print("Oikein!!")
        print(attempts, "attempt(s)")
        break
    elif guess < number:
        print("Liian pieni arvaus!")
    else:
        print("Liian suuri arvaus!")

