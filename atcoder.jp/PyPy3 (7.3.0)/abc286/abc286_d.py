N, X = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

inf = 10 ** 18
dp = [[inf] * (X + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    a, b = AB[i]
    for j in range(X + 1):
        if dp[i][j] < inf:
            dp[i+1][j] = 0
        if j >= a:
            if dp[i][j-a] < inf:
                dp[i+1][j] = min(dp[i+1][j], 1)
            if dp[i+1][j-a] < b:
                dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-a] + 1)

if dp[N][X] < inf:
    print("Yes")
else:
    print("No")
