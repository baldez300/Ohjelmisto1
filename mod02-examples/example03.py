
# Ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

width = int(input("Width: "))
length = int(input("Length: "))

area = width * length
perimeter = 2 * (width + length)

print("The perimeter of the rectangle is: ", perimeter)
print("The area of the rectangle is: ", area)
