import sys
from bisect import bisect_left
from itertools import accumulate

input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
A.sort()
diff = [A[i + 1] - A[i] for i in range(N - 1)]
diff.sort()
pref = list(accumulate([0] + diff))

Q = int(input())
for _ in range(Q):
    left, right = map(int, input().split())
    width = right - left + 1
    idx = bisect_left(diff, width)
    answer = (N - idx) * width + pref[idx]
    print(answer)
