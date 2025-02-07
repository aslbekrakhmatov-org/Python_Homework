number_list = list(map(int, input().split()))
negative_list = []
for x in number_list:
    if x<0:
        negative_list.append(x)
print(sum(negative_list))
