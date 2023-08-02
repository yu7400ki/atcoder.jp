N, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]
V = sum([v for _, v in wv])

inf = 1 << 63
dp = [[inf] * (V+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(V+1):
        if dp[i][j] == inf:
            continue
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        w, v = wv[i]
        if j + v > V:
            continue
        dp[i+1][j+v] = min(dp[i+1][j+v], dp[i][j] + w)

ans = 0
for v in range(V+1):
    if dp[N][v] <= W:
        ans = v
print(ans)
