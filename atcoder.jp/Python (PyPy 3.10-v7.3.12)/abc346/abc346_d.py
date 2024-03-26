N = int(input())
S = list(map(int, list(input())))
C = list(map(int, input().split()))

inf = 1 << 60
dp = [[[inf] * 2 for _ in range(2)] for _ in range(N)]
dp[0][S[0]][0] = 0
dp[0][1 - S[0]][0] = C[0]

for i in range(N - 1):
    for j in range(2):
        for k in range(2):
            if dp[i][j][k] == inf:
                continue
            if k == 0:
                if j == S[i + 1]:
                    dp[i + 1][S[i + 1]][1] = min(dp[i + 1][S[i + 1]][1], dp[i][j][k])
                    dp[i + 1][1 - S[i + 1]][0] = min(
                        dp[i + 1][1 - S[i + 1]][0], dp[i][j][k] + C[i + 1]
                    )
                else:
                    dp[i + 1][S[i + 1]][0] = min(dp[i + 1][S[i + 1]][0], dp[i][j][k])
                    dp[i + 1][1 - S[i + 1]][1] = min(
                        dp[i + 1][1 - S[i + 1]][1], dp[i][j][k] + C[i + 1]
                    )
            else:
                if j == S[i + 1]:
                    dp[i + 1][1 - S[i + 1]][1] = min(
                        dp[i + 1][1 - S[i + 1]][1], dp[i][j][k] + C[i + 1]
                    )
                else:
                    dp[i + 1][S[i + 1]][1] = min(dp[i + 1][S[i + 1]][1], dp[i][j][k])

ans = min(dp[N - 1][0][1], dp[N - 1][1][1])
if ans == inf:
    print(-1)
else:
    print(ans)
