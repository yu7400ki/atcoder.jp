N, K = map(int,input().split())
a = list(map(int,input().split()))
A = sorted(a)

if K == 1:
	print('Yes')
	exit()

for i in range(N - K):
	flag = True
	for j in range(N - K - i):
		if a[j] > a[j+K]:
			flag = False
			a[j], a[j+K] = a[j+K], a[j]
		if flag: break

print('Yes' if a == A else 'No')