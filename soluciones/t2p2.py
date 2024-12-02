from sys import stdin

input = stdin.readline

L, N = map(int, input().split())

while L != 0:
    intervals = []
    for _ in range(N):
        x, r = map(int, input().split())
        intervals.append((x - r, x + r))

    intervals.sort()

    pos = 0
    i = 0
    ans = N

    while pos < L:
        max_reach = pos

        while i < N and intervals[i][0] <= pos:
            max_reach = max(max_reach, intervals[i][1])
            i += 1

        if max_reach == pos:
            break

        pos = max_reach
        ans -= 1

    print(-1 if pos < L else ans)

    L, N = map(int, input().split())
