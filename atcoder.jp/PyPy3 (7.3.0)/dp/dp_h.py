H, W = map(int, input().split())
a = [[s == "." for s in input()] for _ in range(H)]
MOD = 10**9 + 7

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H-1):
    for j in range(W-1):
        dp[i][j+1] += (dp[i][j] * a[i][j+1]) % MOD
        dp[i+1][j] += (dp[i][j] * a[i+1][j]) % MOD

for i in range(H-1):
    dp[i+1][W-1] += (dp[i][W-1] * a[i+1][W-1]) % MOD

for j in range(W-1):
    dp[H-1][j+1] += (dp[H-1][j] * a[H-1][j+1]) % MOD

print(dp[H-1][W-1] % MOD)
