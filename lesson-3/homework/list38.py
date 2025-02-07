list1 = input().split()
list2 = list(reversed(list1))
if list1==list2:
    print("Palindrome")
else:
    print("Not palindrome")