from collections import Counter

def combination(n, r):
    if n < r:
        return 0
    r = min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n - i + 1)
        denom = denom * i
    return numer // denom

N = int(input())
A = list(map(int, input().split()))

acc = [0] * (N + 1)
for i in range(N):
    acc[i + 1] = acc[i] + A[i]
acc.sort()
counter = Counter(acc)

res = 0
for v in counter.values():
    res += combination(v, 2)

print(res)
