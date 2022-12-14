N, M = map(int,input().split())
A = list(map(int,input().split()))

dp = [[-(1 << 63)] * (N+1) for _ in range(M+1)]
dp[0] = [0] * (N+1)

for i in range(1, M+1):
    for j in range(i, N-M+1+i):
        dp[i][j] = max(dp[i][j-1], A[j-1] * i + dp[i-1][j-1])

print(max(dp[-1]))