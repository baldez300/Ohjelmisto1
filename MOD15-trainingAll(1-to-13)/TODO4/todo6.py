import random

# Let's implement an algorithm to calculate the approximate value of pi (π).
# Let's assume that A is a unit circle, i.e. a circle whose center is at the origin and whose radius is one.
# The smallest possible square B is drawn around it so that circle A remains completely inside the square.
# The corner points of the square are then (-1,-1), (1,-1), (1,1) and (-1,1).
# If a large number of points are randomly drawn inside the square,
# a proportion of them will also fall inside the circle
# approximately as large as the area of the circle is of the area of the square, i.e. πr^2/4,
# which (since the radius of the circle is one) narrows down to π/4.
# This provides a simple method for calculating the approximate value of silicon:
# We draw a large number of points in random positions inside the square B, for example a million.
# Let N be this total number of points.
# For each point drawn inside the square B, it is tested in turn whether it also falls inside the unit circle A.
# Let n be the total number of points inside the circle. Now n/N≈π/4 applies, which gives π≈4n/N.
# Write a program that asks the user for the number of points to be scored
# and implements the calculation of the approximate value of the score using the method described above.
# Finally, the program prints the silicon approximation to the user.
# (Note that it is easy to test for each valued point (x,y) whether it is inside the unit circle A:
# it is enough to test whether the point fulfills the inequality x^2+y^2<1.)

point_count = int(input("How many times are points drawn: "))
point_inside_circle = 0

for i in range(point_count):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        point_inside_circle += 1

    pi = point_inside_circle / point_count * 4
    print(f"Pi is {round(pi)} with round")
    print(f"Pi is {pi}")
