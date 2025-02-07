list1= list(map(int, input("Enter the list of integers: ").split()))
even_list = []
for x in list1:
    if x%2==0:
        even_list.append(x)
print(even_list)