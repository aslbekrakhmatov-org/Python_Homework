def is_prime(N):
    if N == 2:
        print(True)
    else:
        for x in range(2,N):
            if N%x==0:
                print(False)
                break
            else:
                print(True)
integer = int(input("N(N>0): "))
is_prime(integer)