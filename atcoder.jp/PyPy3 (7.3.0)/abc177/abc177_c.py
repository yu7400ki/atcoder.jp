N = int(input())
A = list(map(int,input().split()))

A_sum = [0] * (N+1)
for i in range(N):
	A_sum[i+1] = A_sum[i] + A[i]

MOD = 10**9+7

ans = 0
for i in range(N-1):
	ans += A[i] * (A_sum[-1] - A_sum[i+1])
	ans %= MOD

print(ans % MOD)