N, M = map(int,input().split())
P = [int(input()) for _ in range(N)]
P.sort()

dp = [[False] * (M+1) for _ in range(5)]
dp[0][0] = True

ans = 0
for i in range(4):
    for j in range(M+1):
        for k in range(N):
            if dp[i][j]:
                p = P[k]
                if j + p >= M:
                    break
                dp[i+1][j+p] = True
                ans = max(ans, j+p)

print(ans)