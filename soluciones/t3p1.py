PRIME = 2147483647
A, P = map(int, input().split())

if A == 0:
    print(pow(P, P - 1, PRIME))

elif A == 1:
    print(pow(P, P, PRIME))

else:
    n = 1
    tmp = A
    while tmp != 1:
        tmp = (tmp * A) % P
        n += 1

    print(pow(P, (P - 1) // n, PRIME))
