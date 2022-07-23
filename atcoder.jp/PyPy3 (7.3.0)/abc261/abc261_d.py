from collections import defaultdict


N, M = map(int,input().split())
X = list(map(int,input().split()))
CY = defaultdict(int)
for _ in range(M):
    C, Y = map(int,input().split())
    CY[C] = Y

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):  #回数
    for j in range(i+1):  #カウント
        dp[i+1][j+1] = max(dp[i][j] + X[i] + CY[j+1], dp[i+1][j+1])
        dp[i+1][0] = max(dp[i][j], dp[i+1][0])

print(max(dp[-1]))