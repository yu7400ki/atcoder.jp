from collections import Counter


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


k = int(input())
fact = Counter(factorize(k))

ans = 0
for i, cnt in fact.items():
    j = 0
    while cnt > 0:
        tmp = i * (j + 1)
        while tmp % i == 0:
            tmp //= i
            cnt -= 1
        j += 1
    ans = max(ans, i * j)

print(ans)
