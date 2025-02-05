sentence = input("Write a sentence: ")
a = False
for i in sentence:
    if i.isdigit():
        a = True

if a:
    print("There is digit.")  
else:
    print("There is no digit.")   