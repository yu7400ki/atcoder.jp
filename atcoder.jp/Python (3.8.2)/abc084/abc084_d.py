def prime(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for p in range(2,int(n**0.5)+1):
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
    return set(p for p in range(n+1) if is_prime[p])

def like2017(n):
    res = [False] * (n + 1)
    primes = prime(n)
    for p in primes:
        if p == 2:
            continue
        if (p + 1) // 2 in primes:
            res[p] = True
    return res

def accumulate(l):
    res = [0] * (len(l) + 1)
    for i, n in enumerate(l):
        res[i + 1] = res[i] + n
    return res

candidates = like2017(10**5)
acc = accumulate(candidates)

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    print(acc[r + 1] - acc[l])
