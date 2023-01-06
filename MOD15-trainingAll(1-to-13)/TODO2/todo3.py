
# Write a program that asks for the base and height of a rectangle.
# The program prints the perimeter and area of a rectangle.
# The perimeter of a rectangle is the total length of its four sides.

base = int(input("Give the base of a rectangle in number: "))
height = int(input("Give the height of a rectangle in number: "))

perimerter = (base + height) * 2
print(f"The perimeter of the rectangle is : {perimerter}")

area = base * height
print(f"The area of the rectangle is : {area}")