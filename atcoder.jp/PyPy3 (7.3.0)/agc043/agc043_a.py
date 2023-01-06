H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dp = [[float('inf')] * W for _ in range(H)]
dp[0][0] = 1 if S[0][0] == "#" else 0

for y in range(H):
    for x in range(W):
        # x + 1, y
        if x + 1 < W:
            if S[y][x + 1] == ".":
                dp[y][x + 1] = min(dp[y][x + 1], dp[y][x])
            else:
                if S[y][x] == ".":
                    dp[y][x + 1] = min(dp[y][x + 1], dp[y][x] + 1)
                else:
                    dp[y][x + 1] = min(dp[y][x + 1], dp[y][x])

        # x, y + 1
        if y + 1 < H:
            if S[y + 1][x] == ".":
                dp[y + 1][x] = min(dp[y + 1][x], dp[y][x])
            else:
                if S[y][x] == ".":
                    dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] + 1)
                else:
                    dp[y + 1][x] = min(dp[y + 1][x], dp[y][x])

print(dp[-1][-1])
