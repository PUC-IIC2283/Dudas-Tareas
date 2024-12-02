from math import log2, ceil
from cmath import exp, pi


N, M = map(int, input().split())
D = input()
T = input()[::-1]

N_PAD = 2 ** ceil(log2(N))
SIGMA = set(T)

TARGET = {}
DOCUMENT = {}
COUNTS = {}


def precompute():
    for letter in SIGMA:
        target = [int(c == letter) for c in T] + [0] * (N_PAD - M)
        TARGET[letter] = fft(target, N_PAD)
        COUNTS[letter] = sum(target)
        DOCUMENT[letter] = [int(c == letter) for c in D] + [0] * (N_PAD - N)


def expand(array: list, f: int):
    temp = [0] * len(array)
    dist = f + 1
    for i in range(len(array)):
        if array[i] == 1:
            dist = 0
        if dist <= f:
            temp[i] = 1
        dist += 1

    dist = f + 1
    for i in range(len(array) - 1, -1, -1):
        if array[i] == 1:
            dist = 0
        if dist <= f:
            temp[i] = 1
        dist += 1

    for i in range(N, N_PAD):
        temp[i] = 0

    return temp


def fft(array: list, n: int):
    if n == 1:
        return array

    mid = n >> 1
    y_0 = fft(array[0::2], mid)
    y_1 = fft(array[1::2], mid)

    y = [0] * n
    alpha = 1
    w = exp(2j * pi / n)
    for k in range(mid):
        a = y_0[k]
        b = alpha * y_1[k]
        y[k] = a + b
        y[mid + k] = a - b
        alpha *= w

    return y


def convolve(array, letter):
    fft_1 = fft(array, N_PAD)
    fft_2 = TARGET[letter]

    fft_result = [a * b for a, b in zip(fft_1, fft_2)]

    fft_inversed = [fft_result[0]] + list(reversed(fft_result[1:]))
    result = [round(x.real / N_PAD) for x in fft(fft_inversed, N_PAD)]

    return result


def eval_f(f):
    results = []
    count_target = []

    for letter in SIGMA:
        substring = DOCUMENT[letter]
        expanded = expand(substring, f)
        mult = convolve(expanded, letter)
        results.append(mult)
        count_target.append(COUNTS[letter])

    results = list(zip(*results))
    f_value = results.count(tuple(count_target))

    return f_value


precompute()
left = 0
right = N
while left < right:
    mid = (left + right) >> 1
    if eval_f(mid) < N - M + 1:
        left = mid + 1
    else:
        right = mid

print(left)
