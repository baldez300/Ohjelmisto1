# Librery  for week2 programming


"""def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    print(final_list)
# Driver code
list1 = []
list1 = "Anna numero: "

# five_largest_numbers = []
while True:
    nums = input(list1)
    list1 = "Anna toinen numero: "
    if nums == '':
        break
N = 5
# Calling the function
Nmaxelements(list1, N) """
#=========
luvut = []

luku = input("Anna ensimmäinen luku tai lopeta painamalla Enter: ")
while luku != "":
    luvut.append(luku)
    luvut.sort(reverse=True)
    luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")

for n in luvut:
    print(f"{n}")
