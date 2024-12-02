import sys

input = sys.stdin.readline

PRIME = (1 << 31) - 1
POWERS = {}


def mult(A, B):
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            c = 0
            for k in range(N):
                c += A[i][k] * B[k][j]

            C[i][j] = c % PRIME

    return C


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

POWERS[0] = A
for i in range(1, 15 + 1):
    POWERS[i] = mult(POWERS[i - 1], POWERS[i - 1])

Q = int(input())

for _ in range(Q):
    exp = int(input())
    binary = reversed(format(exp, "b"))
    to_mult = [i for i, bit in enumerate(binary) if bit == "1"]

    result = POWERS[to_mult[0]]
    for i in to_mult[1:]:
        result = mult(result, POWERS[i])

    print(sum((sum(c) for c in result)) % PRIME)
