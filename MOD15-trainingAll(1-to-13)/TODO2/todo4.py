
# Write a program that asks for three integers.
# The program prints the sum, product and average of the numbers.

num1 = int(input("Give first number: "))
num2 = int(input("Give second number: "))
num3 = int(input("Give third number: "))

nums_sum = num1 + num2 + num3
nums_product = num1 * num2 * num3
nums_average = nums_sum / 3

print(f"The sum of the three numbers are: {nums_sum}")
print(f"The product of the three numbers are: {nums_product}")
print(f"The average of the three numbers are: {nums_average:.2f}")