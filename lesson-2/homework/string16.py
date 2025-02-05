string = input("Enter a string: ")
charc = input("Enter a character: ")
if charc in string:
    new_string=string.replace(charc, "")
print(new_string)
