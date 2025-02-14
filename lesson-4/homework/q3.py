txt = input()
done = {'a', 'u', 'e', 'i', 'o'}
count = 0
result = []

for x in range(len(txt)): #iterate through elements of string(txt)
    count+=1 # counts every third element
    result.append(txt[x]) # adds the element - the reason of writing this code in this line earlier is that underscore always is added after the elemet
    if x!=len(txt)-1 and count>=3 and txt[x] not in done:
        done.add(txt[x])
        result.append("_")
        count=0

print("".join(result))
