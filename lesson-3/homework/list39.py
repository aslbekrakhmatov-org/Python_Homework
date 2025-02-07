org_list = input("Enter a list: ").split()
sublist_length = int(input("Enter the number of elements in sublist: "))
nested_list = [org_list[x:x+sublist_length] for x in range(0,len(org_list), sublist_length)]
print(nested_list)

