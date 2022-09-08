# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa
# kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random
def main(max_num):

    min_num = 1
    while True:
        r = random.randint(min_num, max_num)
        print(r)
        if r == 21:
            break


dice = int(input("Hei, voit heitellä numeroa 21: "))
main(dice)