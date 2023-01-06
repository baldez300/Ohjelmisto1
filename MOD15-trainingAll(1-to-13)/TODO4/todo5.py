
# Write a program that asks the user for a username and password.
# If either or both are wrong, the ID and password will be asked again.
# This continues until the login information is correct or the wrong information has been entered five times.
# In the former case, 'Welcome' is printed, and in the latter, 'Access Denied'.
# (The correct username is 'python' and the password is 'rules').

user = "python"
password = "rules"
count = 1

while True:
    ui_user = input("Enter your user name: ")
    pass_user = input("Enter your password: ")

    if ui_user == user and pass_user == password:
        print("welcome")
        break
    elif count == 5:
        print("Access Denied")
        break

    count += 1

# Second way to do the same thing
attempts = 5

while attempts:
    user_name = input("User name: ")
    password = input("Password: ")

    if user_name == "python" and password == "rules":
        print("You are welcome!")
        break

    attempts -= 1
    print(f"Username or password is incorrect. Try again '{attempts} attempt(s) left'")
else:
    print("Accessed denied.")