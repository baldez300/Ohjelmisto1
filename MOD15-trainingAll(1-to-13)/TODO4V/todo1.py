
# Some while loop
i = 0
while i < 10:
    i += 1
    print(i)
else:  # This executes when the while loop ends naturally
    print("Ended!\n")

# Break the while execution
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 4:
        print("Game over!")
        break
    else:
        print("Over?")