list1 = input("Enter the first list: ").split()
sub_list = input("Enter the sublist: ").split()
a = False
for x in sub_list:
    if x in list1:
        a = True
if a:
    print("True")
