from collections import defaultdict

N = int(input())
snuke = defaultdict(lambda : (0, 0))
for _ in range(N):
    T, X, A = map(int, input().split())
    snuke[T] = (X, A)

dp = [[0] * 5 for _ in range(T+1)]
for i in range(T):
    for j in range(min(i+1, 5)):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + (snuke[i+1][1] if snuke[i+1][0] == j else 0))
        if j > 0:
            dp[i+1][j-1] = max(dp[i+1][j-1], dp[i][j] + (snuke[i+1][1] if snuke[i+1][0] == j-1 else 0))
        if j < 4:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + (snuke[i+1][1] if snuke[i+1][0] == j+1 else 0))

print(max(dp[-1]))