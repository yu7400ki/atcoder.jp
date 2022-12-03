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


def a(n):
    if n < 3:
        return 1
    else:
        a = 1
        b = 1
        c = -1 * ((n - 1) * 2 + 2)
        D = b ** 2 - 4 * a * c
        return ceil((-b + D ** 0.5) / (2 * a))


k = int(input())
fact = Counter(factorize(k))

ans = 0
for i, cnt in fact.items():
    ans = max(ans, a(cnt) * i)

print(ans)
