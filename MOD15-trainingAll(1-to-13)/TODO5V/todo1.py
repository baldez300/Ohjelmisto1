
# Training
first_names = ["John", "Jane", "Joe", "Jill", "Jack", "Jenny"]

print(first_names[0])
print(first_names[2])
print(first_names[-2])
print(first_names[1:3])
print(first_names[3:3])

print(first_names[-1:-3])
print(first_names[-1][0:1])

print(first_names[0:5:2])

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[1::2])
print(num[:-3])

first_names.remove("Joe")

first_names.extend(num)

print(num)
print(first_names)

print(first_names.index(5))  # It returns the index number

if "Jill" in first_names:
    print("Jill is on the list")

first_names = ["John", "Jane", "Joe", "Jill", "Jack", "Jenny"]
first_names.sort()
print(first_names)

first_names.sort(reverse=True)
print(first_names)