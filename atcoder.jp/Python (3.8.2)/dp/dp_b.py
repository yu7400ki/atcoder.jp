N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [1 << 63] * N
dp[0] = 0

for i in range(N-1):
    for k in range(1, min(N-i, K+1)):
        j = i + k
        dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j]))

print(dp[N-1])
