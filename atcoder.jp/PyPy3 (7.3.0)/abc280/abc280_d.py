from collections import Counter
from math import ceil


def factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


k = int(input())
fact = Counter(factorize(k))

ans = 0
for i, cnt in fact.items():
    ans = max(ans, cnt * i)

print(ans)
