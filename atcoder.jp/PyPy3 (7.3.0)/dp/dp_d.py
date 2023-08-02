N, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(W):
        if dp[i][j] == -1:
            continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        w, v = wv[i]
        if j + w > W:
            continue
        dp[i+1][j+w] = max(dp[i+1][j+w], dp[i+1][j] + v)

print(max(dp[N]))
