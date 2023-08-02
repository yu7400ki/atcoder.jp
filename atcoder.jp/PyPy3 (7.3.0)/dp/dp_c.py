N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = abc[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + abc[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + abc[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + abc[i][2]

print(max(dp[N-1]))
