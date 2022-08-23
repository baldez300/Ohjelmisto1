# Module2, Syöte- ja muuttujan esmerkkejä

username = "Kalle"
# int
age = 6
age = age + 1
# float value
wallet_balance = 15.40

fullname = "Kalle Kontio"
 # merkijonejen littäminen
user = username + " (" + fullname + ")"
print("Käyttäjä on: ", user + " on " + str(age) + " vuotta")
print("Hänellä on loppakossa  ",  wallet_balance, "euro")
ticket_price = input(username + " osti bussilipun hinta: ")
wallet_balance = wallet_balance - float(ticket_price)
print(f"Hänellä on loppakossa    {wallet_balance:.2f}  euro")

# username = input("Kuka olet?")
# print("Hei", username, "!")

# username = input("Kuka sitten olet??")
# print("Hei", username, "!")