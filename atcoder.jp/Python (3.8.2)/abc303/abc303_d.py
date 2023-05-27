X, Y, Z = map(int, input().split())
S = list(input())

dp = [[-1] * 2 for _ in range(len(S) + 1)]
dp[0][0] = 0
dp[0][1] = Z

for i, s in enumerate(S):
    dp[i][0] = min(dp[i][0], dp[i][1] + Z)
    dp[i][1] = min(dp[i][0] + Z, dp[i][1])
    if s == "a":
        dp[i + 1][0] = dp[i][0] + X
        dp[i + 1][1] = dp[i][1] + Y
    elif s == "A":
        dp[i + 1][0] = dp[i][0] + Y
        dp[i + 1][1] = dp[i][1] + X

print(min(dp[-1][0], dp[-1][1]))
