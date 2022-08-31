
# Ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

# take inputs
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

# calculate sum
sum_of_int = num1 + num2 + num3

# calculate product
product = num1 * num2 * num3

# calculate average
avg = sum_of_int / 3

# display result
print('The sum of the numbers = %.0f' % sum_of_int)
print('The product of the numbers = %.0f' % product)
print('The average of the numbers = %0.2f' % avg)
