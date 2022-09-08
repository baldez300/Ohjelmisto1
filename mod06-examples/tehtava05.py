# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen
# kuin parametrina saatu lista paitsi että siitä on karsittu pois
# kaikki parittomat luvut. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
def remove_odd(lst):
    even_num = []
    for i in range(len(lst)):
        print(lst[i])
        if(lst[i] % 2 == 0):
            even_num.append(lst[i])
    return even_num


# creating an empty list
numbers_list = []
# number of elemetns as input
n = int(input("Enter number of elements in the list : "))
# iterating till the range
for i in range(0, n):
    ele = int(input("Add number: "))
    numbers_list.append(ele) # adding the element
print("After odd numbers were removed: ", remove_odd(numbers_list))