list1 = input("Enter the first list: ").split()
list2 = input("Enter the second list: ").split()
uncommon = []
for x in list1:
    if x not in list2:
        uncommon.append(x)
for y in list2:
    if y not in list1:
        uncommon.append(y)
print(uncommon)

