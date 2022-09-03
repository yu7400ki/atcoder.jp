N, M = map(int,input().split())
A = list(map(int,input().split()))

dp = [[0] * (N+1) for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        dp[i][j] = max(dp[i][j-1], A[j-1] * i + dp[i-1][j-1])

print(max(dp[-1]))