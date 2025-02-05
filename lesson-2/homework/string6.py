string1=input("Enter a string: ")
string2=input("Enter another string: ")
if string1 in string2 or string2 in string1:
    print("One string contains another.")
else:
    print('One string doesn\'t contain another.')
    