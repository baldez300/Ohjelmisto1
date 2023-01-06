import math

# Write a program that asks for the radius of a circle and prints its area.

radius = int(input("Give the radius of a circle: "))
area = 3.14 * radius * radius
print(f"The area of the circle is: {area} \n")

# Second way
print("Calculate the circle's surface")
rad = int(input("Give the radius in meters: "))
print(f"{rad} (m) the area of the circle is: {(math.pi * rad ** 2):.3f} square meters")
