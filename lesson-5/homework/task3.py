def factors(N):
    for x in range(1,N+1):
        if N%x==0:
            print(f"{x} is a fator of {N}")

num = int(input("Enter a positive integer: "))
factors(num)