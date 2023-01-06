import math


# Write a function that receives as parameters the diameter of a round pizza in centimeters
# and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza in euros per square meter.
# The main program asks the user for the diameters and prices of two pizzas
# and indicates which pizza gives better value for money (i.e. which one has a lower unit price).
# The written function must be used in the calculation of unit prices.

def calculate_pizza_price(diameter, price):
    square_centimeter = (diameter / 2) ** 2 * math.pi
    square_meter = square_centimeter / 10_000
    return square_meter * price


pizzas = []
for pizza_name in ["A", "B"]:
    diameter_x = float(input(f"{pizza_name}). Enter the diameter of the pizza in centimeters: "))
    price_x = float(input(f"{pizza_name}). Enter the price of the pizza in euros: "))
    pizzas.append(price_x)
    print(f"{pizza_name}). The unit price is: {calculate_pizza_price(diameter_x, price_x):.2f} €/m2\n")

if pizzas[0] < pizzas[1]:
    print("A). pizza is cheaper")
elif pizzas[0] > pizzas[1]:
    print("B). pizza is cheaper")
else:
    print("Pizzas are the same price.")