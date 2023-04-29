def prime(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for p in range(2,int(n**0.5)+1):
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
    return [p for p in range(n+1) if is_prime[p]]

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

a_limit = (10 ** 12) ** (1 / 5)
c_limit = ((10 ** 12) / 12) ** 0.5

primes = prime(int(c_limit))

N = int(input())

ans = 0
for i in range(len(primes)):
    a = primes[i]
    if a > a_limit:
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if a ** 2 * b > N:
            break
        ok = binary_search(primes, (N // (a ** 2 * b)) ** 0.5, ok = j)
        if ok == j:
            break
        ans += ok - j

print(ans)
