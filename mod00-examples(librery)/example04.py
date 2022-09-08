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
input_string = input("Enter a list element separated by space ")
list  = input_string.split()
print("Calculating sum of element of input list")
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)
