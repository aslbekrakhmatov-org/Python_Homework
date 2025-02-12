prime_numbers = []
primenum_checker = False
for x in range(2,100):
    if x==2:
        prime_numbers.append(x)
    else:
        for y in range(2,x):
            if x%y==0:
                primenum_checker = False
                break
            else:
                primenum_checker = True
    if primenum_checker:
        prime_numbers.append(x)

print(prime_numbers)