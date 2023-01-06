
# Write a program that asks the user's biological sex and hemoglobin value (g/l).
# The program indicates whether the hemoglobin value is low, normal or high.
# A woman's normal hemoglobin value is between 117-175 g/l.
# A man's normal hemoglobin value is between 134-195 g/l.

print("We calculate whether your hemoglobin value is OK")

gender = input("Are you a male or female? (M/F): ").upper()
hemoglobin_value = float(input("Give your hemoglobin value (g/l): "))

if gender == "F":
    if hemoglobin_value < 117:
        print("Your hemoglobin is down")
    elif hemoglobin_value <= 175:
        print("Your hemoglobin is normal")
    else:
        print("Your hemoglobin is high")
elif gender == "M":
    if hemoglobin_value < 134:
        print("Your hemoglobin is down")
    elif hemoglobin_value <= 195:
        print("Your hemoglobin is normal")
    else:
        print("Your hemoglobin is high")
else:
    print("We don't support your gender :D")
