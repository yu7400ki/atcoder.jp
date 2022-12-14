N = int(input())

def prime(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for p in range(2,int(n**0.5)+1):
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
    return [i for i in range(n+1) if is_prime[i]]

limit = int(pow(N, 1/3))+1
primes = prime(limit)

cnt = 0
length = len(primes)
for i in range(length-1):
    ok = i
    ng = length
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if primes[mid] ** 3 * primes[i] <= N:
            ok = mid
        else:
            ng = mid
    cnt += ok - i

print(cnt)