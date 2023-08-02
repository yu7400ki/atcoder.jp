s = list(input())
t = list(input())

dp = [[""] * (len(s) + 1) for _ in range(len(t) + 1)]

for i in range(1, len(t)+1):
    for j in range(1, len(s)+1):
        if t[i-1] == s[j-1]:
            dp[i][j] = dp[i-1][j-1] + t[i-1]
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1], key=len)

print(dp[-1][-1])
