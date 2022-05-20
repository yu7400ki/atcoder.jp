N = int(input())
MOD = 998244353

dp = [[0] * 11 for _ in range(N)]
for i in range(9):
    dp[0][i+1] = 1

for i in range(1,N):
    for j in range(1,10):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % MOD


print(sum(dp[-1]) % MOD)