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

cnt = 0
for i in range(len(primes)):
	for j in range(i + 1, len(primes)):
		if primes[j]**3 * primes[i] <= n:
			cnt += 1
		else:
			break

print(cnt)