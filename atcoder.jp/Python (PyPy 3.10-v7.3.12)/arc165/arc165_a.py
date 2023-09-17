from collections import Counter

def prime_factorize(n):
    res = []
    while n & 1 == 0:
        res.append(2)
        n >>= 1
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            res.append(i)
            n //= i
    if n != 1:
        res.append(n)
    return res

def solve():
    N = int(input())
    primes = Counter(prime_factorize(N))
    if len(primes) == 1:
        print("No")
    else:
        print("Yes")

T = int(input())
for _ in range(T):
    solve()
