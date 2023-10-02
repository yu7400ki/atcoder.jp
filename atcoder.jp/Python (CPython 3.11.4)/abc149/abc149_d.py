N, K = map(int, input().split())
SCORE = list(map(int, input().split()))
T = list(map(lambda s: 0 if s == "r" else 1 if s == "s" else 2, list(input())))

dp = [[-1] * 3 for _ in range(N)]

for k in range(K):
    for i in range(3):
        if (T[k] - i) % 3 == 1:
            score = SCORE[i]
        else:
            score = 0
        dp[k][i] = score
    for k in range(k + K, N, K):
        for i in range(3):
            for j in range(3):
                if j == i:
                    continue
                if (T[k] - i) % 3 == 1:
                    score = SCORE[i]
                else:
                    score = 0
                dp[k][i] = max(dp[k][i], dp[k - K][j] + score)

ans = 0
for i in range(K):
    ans += max(dp[N - i - 1])

print(ans)
