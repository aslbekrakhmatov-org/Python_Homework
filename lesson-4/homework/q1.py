list1 = input("Enter the first list: ").split()
list2 = input("Enter the second list: ").split()
set1 = set(list1)
set2 = set(list2)
uncommon = list(set1.symmetric_difference(set2))
print(uncommon)

