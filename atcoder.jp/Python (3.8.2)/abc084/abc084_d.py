def prime(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for p in range(2,int(n**0.5)+1):
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
    return set(p for p in range(n+1) if is_prime[p])

def like2017(n):
    res = []
    primes = prime(n)
    for p in primes:
        if p == 2:
            continue
        if (p + 1) // 2 in primes:
            res.append(p)
    res.sort()
    return res

def binary_search(lst, target, ok = -1, ng = None, key = None):
    ng = len(lst) if ng is None else ng
    key = (lambda x: lst[x] <= target) if key is None else key

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key(mid):
            ok = mid
        else:
            ng = mid

    return ok

candidates = like2017(10**5)

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    lower = binary_search(candidates, l, ok = len(candidates), ng = -1, key = lambda x: candidates[x] >= l)
    upper = binary_search(candidates, r)
    print(upper - lower + 1)
