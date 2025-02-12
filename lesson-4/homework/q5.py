password = input("Create a password: ")
uppercase_checker = False
if len(password)>=8:
    for x in password:
        if x.isupper():
            uppercase_checker=True
            break
    if uppercase_checker:
        print("Password is strong.")
    else:
        print("Password must contain an uppercase letter.")
            
else:
    print("Password is too short")