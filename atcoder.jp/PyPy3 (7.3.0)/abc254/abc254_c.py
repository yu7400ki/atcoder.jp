N, K = map(int,input().split())
a = list(map(int,input().split()))
A = sorted(a)

for i in range(N - K):
	for j in range(N - K - i):
		if a[j] > a[j+K]:
			a[j], a[j+K] = a[j+K], a[j]

print('Yes' if a == A else 'No')