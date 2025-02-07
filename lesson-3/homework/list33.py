list1 = [1, 2, 1, 'a', 'b', 'a', 'c', '!']
element = "a"
indices = []
for x in range(len(list1)):
    if element==list1[x]:
        indices.append(x)
print(indices)
