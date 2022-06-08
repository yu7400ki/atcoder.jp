N, M = map(int,input().split())
A = list(map(int,input().split()))[::-1]
C = list(map(int,input().split()))[::-1]

ans = [0] * (M+1)
for i in range(M+1):
	div = C[i] // A[0]
	ans[i] = div
	for j in range(N+1):
		C[i+j] -= A[j] * div

print(*ans[::-1])