n = int(input())

num = 5
primes = [2, 3]
while True:
	for i in primes:
		if i**2 > num:
			primes.append(num)
			break
		if num % i == 0:
			break
	else:
		primes.append(num)
	num += 2
	if num >= pow(10**18,1/3):
		break

cnt = 0
for i in range(len(primes)):
	for j in range(i+1,len(primes)):
		if primes[j] ** 3 * primes[i] <= n:
			cnt += 1
		else:
			break
print(cnt)