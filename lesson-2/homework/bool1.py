username = input("Username: ")
password = input("Password: ")

if not bool(username.strip() and password.strip()):
    print("Please enter your username and password!")
else:
    print("Your username:", username, "\nYour password:", password)
