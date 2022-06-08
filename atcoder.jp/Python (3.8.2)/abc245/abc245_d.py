N, M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = [0] * (M+1)
for i in range(M+1):
	div = C[i] // A[0]
	ans[i] = div
	for j in range(N+1):
		C[j+i] -= A[j] * div

print(*ans)