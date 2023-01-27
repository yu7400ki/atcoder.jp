from collections import Counter

N = int(input())
MOD = 10 ** 9 + 7

def prime_factorize(n):
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

factors = []
for i in range(1, N + 1):
    factors.extend(prime_factorize(i))
factors = Counter(factors)

ans = 1
for v in factors.values():
    ans *= v + 1
    ans %= MOD

print(ans)
