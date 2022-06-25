N, K, Q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))

C = [False] * N
for i in A:
	C[i-1] = True

for i in L:
	cnt = 0
	idx = 0
	while True:
		if C[idx]:
			cnt += 1
		if i == cnt: break
		idx += 1
	if idx+1 == N: continue
	if C[idx]:
		if not C[idx+1]:
			C[idx], C[idx+1] = C[idx+1], C[idx]

print(*[i+1 for i in range(N) if C[i]])