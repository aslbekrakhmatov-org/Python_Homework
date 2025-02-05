string = input("Enter a string: ")
vowels = "aeuioAEUIO"
new_string = ""
for i in string:
    if i in vowels:
        new_string+="*"
    else:
        new_string+=i
print(new_string)        


