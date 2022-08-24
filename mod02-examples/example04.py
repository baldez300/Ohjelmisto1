
# Ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# calculate sum
sum0 = num1 + num2 + num3

# calculate product
product = num1 * num2 * num3

# calculate average
avg = (num1 + num2 + num3)/3

# display result
print('The sum of the numbers = %0.2f' % sum0)
print('The product of the numbers = %0.2f' % product)
print('The average of the numbers = %0.2f' % avg)
