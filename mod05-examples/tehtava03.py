# Ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

"""# taking input from user
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")"""

# Toinen versio ratkaisu alaspain ========================

number = int(input("Enter any number: "))
alkuluku = True

for i in range(2, number):
    if (number % i) == 0: alkuluku = False

if alkuluku:
    print(number, "is a prime number")

else:
    print(number, "is not a prime number")
