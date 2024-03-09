T = input()
N = int(input())
S = [input().split()[1:] for _ in range(N)]

inf = 1 << 60
dp = [[inf] * (len(T) + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(len(T) + 1):
        if dp[i][j] == inf:
            continue
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        for s in S[i]:
            if j + len(s) <= len(T) and T[j : j + len(s)] == s:
                dp[i + 1][j + len(s)] = min(dp[i + 1][j + len(s)], dp[i][j] + 1)

print(dp[N][len(T)] if dp[N][len(T)] < inf else -1)
