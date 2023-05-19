N = int(input())
S = list(input())

MOD = 10 ** 9 + 7
T = ["a", "t", "c", "o", "d", "e", "r"]

dp = [[0] * 8 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(8):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
        if j == 7: continue
        if S[i] == T[j]:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD

print(dp[N][7] % MOD)
