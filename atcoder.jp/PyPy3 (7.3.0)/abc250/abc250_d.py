n = int(input())

primes = [2, 3]
for i in range(5, int(pow(n,1/3))+1, 2):
	for j in primes:
		if j**2 > i:
			primes.append(i)
			break
		if i % j == 0:
			break
	else:
		primes.append(i)

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