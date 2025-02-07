list1 = input("Enter a list: ").split()
n = int(input("Enter a number: "))
new_list = []
for x in list1:
    new_list.extend(x*n)
print(new_list)