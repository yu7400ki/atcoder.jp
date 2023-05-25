N = int(input())
DCS = [tuple(map(int, input().split())) for _ in range(N)]
DCS.sort(key=lambda x: x[0])

d_ma = max(dcs[0] for dcs in DCS)
dp = [[-1] * (d_ma + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(d_ma + 1):
        if dp[i][j] == -1:
            continue
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        dcs = DCS[i]
        if j + dcs[1] > dcs[0]:
            continue
        dp[i + 1][j + dcs[1]] = max(dp[i + 1][j + dcs[1]], dp[i][j] + dcs[2])

print(max(dp[N]))
