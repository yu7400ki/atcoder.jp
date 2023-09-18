S = list(input())
N = len(S)
MOD = 10**9+7

chokudai = list("chokudai")
dp = [[0] * (len(chokudai) + 1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(len(chokudai)+1):
        if dp[i][j] == 0:
            continue
        if j < len(chokudai) and S[i] == chokudai[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= MOD

print(dp[-1][-1])
