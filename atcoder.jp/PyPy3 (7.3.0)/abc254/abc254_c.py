N, K = map(int,input().split())
a = list(map(int,input().split()))
A = sorted(a)

div = [[] for _ in range(K)]
for i in range(N):
	div[i % K].append(a[i])

div = [sorted(e) for e in div]

res = [0] * N
for i in range(len(div)):
	for j in range(len(div[i])):
		res[j*K+i] = div[i][j]

print('Yes' if res == A else 'No')