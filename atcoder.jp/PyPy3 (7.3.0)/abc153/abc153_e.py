H, N = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

dp = [float("inf")] * (H + 1)
dp[0] = 0

for i in range(H):
    if dp[i] == float("inf"):
        continue

    for a, b in AB:
        if i + a > H:
            dp[H] = min(dp[H], dp[i] + b)
        else:
            dp[i + a] = min(dp[i + a], dp[i] + b)

print(dp[H])
