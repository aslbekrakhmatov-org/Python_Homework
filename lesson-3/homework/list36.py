number_list = list(map(int, input().split()))
positive_list = []
for x in number_list:
    if x>0:
        positive_list.append(x)
print(sum(positive_list))

