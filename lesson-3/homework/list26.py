list1 = input().split()
length = len(list1)
if length%2==0:
    print("Middle elements: ", list1[(length//2-1) : (length//2+1)])
else:
    print("Middle element: ", list1[(length//2)])

