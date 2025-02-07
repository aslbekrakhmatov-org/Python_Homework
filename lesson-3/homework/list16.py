list1= list(map(int, input("Enter the list of integers: ").split()))
odd_list = []
for x in list1:
    if x%2!=0:
        odd_list.append(x)
print(odd_list)