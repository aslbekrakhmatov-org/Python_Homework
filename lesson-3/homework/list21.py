list1 = list(map(int, input("Enter the list of numbers: ").split()))
for x in list1:
    if x==min(list1):
        list1.remove(x)
print(min(list1))