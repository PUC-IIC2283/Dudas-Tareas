PRIME = 2147483647
N = int(input())
FAC = [1] * N
IFAC = [1] * N
V = [[] for _ in range(N + 1)]
DP = [[[0] * 2 for _ in range(N + 1)] for _ in range(N + 1)]
G = [[0] * 2 for _ in range(N + 1)]
SIZE = [0] * (N + 1)
ANS = [0] * N


def binom(n, m):
    return (FAC[n]) * ((IFAC[m] * IFAC[n - m]) % PRIME) % PRIME


def dfs(x, father):
    SIZE[x] = 1
    DP[x][0][0] = DP[x][0][1] = 1

    for i in range(len(V[x])):
        neighbor = V[x][i]
        if neighbor == father:
            continue

        dfs(neighbor, x)

        for j in range(SIZE[x] + SIZE[neighbor] + 1):
            G[j][0] = G[j][1] = 0

        for j in range(SIZE[x]):
            for k in range(SIZE[neighbor]):
                G[j + k][0] += DP[x][j][0] * DP[neighbor][k][1]
                G[j + k][1] += DP[x][j][1] * DP[neighbor][k][1]
                G[j + k + 1][0] += DP[x][j][0] * DP[neighbor][k][0]
                G[j + k + 1][1] += (DP[x][j][1] * DP[neighbor][k][0]) + (
                    DP[x][j][0] * DP[neighbor][k][1]
                )

        for j in range(SIZE[x] + SIZE[neighbor] + 1):
            DP[x][j][0] = G[j][0] % PRIME
            DP[x][j][1] = G[j][1] % PRIME

        SIZE[x] += SIZE[neighbor]


for i in range(1, N):
    x, y = map(int, input().split())
    V[x].append(y)
    V[y].append(x)
    FAC[i] = FAC[i - 1] * i % PRIME
    IFAC[i] = pow(FAC[i], PRIME - 2, PRIME)

dfs(1, 0)

for j in range(N - 1, -1, -1):
    ANS[j] = DP[1][j][1]
    if j == N - 1:
        ANS[j] = 1

    else:
        ANS[j] = (ANS[j] * pow(N, N - j - 2, PRIME)) % PRIME

    for k in range(j + 1, N):
        ANS[j] = (ANS[j] - (ANS[k] * binom(k, j)) % PRIME) % PRIME

print("\n".join(map(str, ANS)))
