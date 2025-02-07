list1 = input("First list: ").split()
list2 = input("Second list: ").split()
new_sorted_list = []
for x in list1:
    new_sorted_list.append(x)
for i in list2:
    if i not in new_sorted_list:
        new_sorted_list.append(i)
print(new_sorted_list)

