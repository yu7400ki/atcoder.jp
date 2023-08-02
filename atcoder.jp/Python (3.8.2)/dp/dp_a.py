N = int(input())
h = list(map(int, input().split()))

dp = [1 << 63] * N
dp[0] = 0

for i in range(N-2):
    dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
    dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]))
dp[N-1] = min(dp[N-1], dp[N-2] + abs(h[N-2] - h[N-1]))

print(dp[N-1])
