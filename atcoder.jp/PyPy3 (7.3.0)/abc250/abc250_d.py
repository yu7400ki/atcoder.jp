n = int(input())

x = int(pow(n,1/3))+1
is_prime = [True] * (x+1)
is_prime[0] = is_prime[1] = False
for p in range(2, int(x ** 0.5) + 1):
    if is_prime[p]:
        for i in range(p*p, x+1, p):
            is_prime[i] = False
primes =  [p for p in range(x + 1) if is_prime[p]]

primes = [0] + primes + [0]

cnt = 0
for i in range(1,len(primes)-1):
	ok = i
	ng = len(primes) - 1
	while ng - ok > 1:
		mid = (ok + ng) // 2
		if primes[mid] ** 3 * primes[i] <= n:
			ok = mid
		else:
			ng = mid
	cnt += ok - i

print(cnt)