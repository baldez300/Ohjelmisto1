import random

# Write a program that draws and prints two different number lock codes:
# a three-digit code, each digit of which is between 0..9.
# a four-digit code, each digit of which is between 1..6.
# Tip: learn how to use the random.randint() function.

three_digit_code = ""
for i in range(3):
    three_digit_code += str(random.randint(0, 9))

four_digit_code = ""
for i in range(4):
    four_digit_code += str(random.randint(1, 6))

print(three_digit_code + "\n" + four_digit_code)
