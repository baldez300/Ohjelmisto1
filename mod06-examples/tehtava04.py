# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

def sum_of_nums(numbers):
    print("Calculating sum of inegers of input list")
    sum_toal = 0
    for num in numbers:
        sum_toal += int(num)
    print("Sum = ", sum_toal)


input_string = input("Enter a list of whole numbers separated by space: ")
lst = input_string.split()
sum_of_nums(lst)