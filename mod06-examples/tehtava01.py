# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
# nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa
# niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
def main():
    min_num, max_num = 1, 6

    while True:
        r = random.randint(min_num, max_num)
        print(r)
        if r == 6:
            break
main()