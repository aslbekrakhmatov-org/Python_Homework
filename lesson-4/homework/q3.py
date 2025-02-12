s = input()  
vowels = "aeiou"
result = []
count = 0  
skip_next = False 

i = 0
while i < len(s):
    if skip_next:  
        result.append(s[i])
        skip_next = False
        i += 1
        count += 1
        continue

    result.append(s[i])
    count += 1
    
    if count == 3:  
        if s[i] in vowels:
            if i + 1 < len(s):  
                result.append(s[i + 1])  
                result.append("_")  
                skip_next = True  
                i += 1  
        else:
            result.append("_")
        
        count = 0  
    
    i += 1


print("".join(result))


