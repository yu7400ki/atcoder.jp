N = int(input())
p = list(map(int, input().split()))

sum_p = sum(p)
dp = [[0] * (sum_p + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(sum_p):
        if dp[i][j] == 0:
            continue
        dp[i+1][j] = dp[i][j]
        dp[i+1][j+p[i]] += dp[i][j]

ans = sum(dp[N])
print(ans)
