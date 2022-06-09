N, M, K = map(int,input().split())
MOD = 998244353

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
	for j in range(K):
		for k in range(1,min(M, K-j)+1):
			dp[i+1][j+k] += dp[i][j]
			dp[i+1][j+k] %= MOD

print(sum(dp[-1]) % MOD)