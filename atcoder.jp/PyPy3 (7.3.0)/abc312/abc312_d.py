S = list(input())
N = len(S)

MOD = 998244353

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for idx in range(N):
    for cnt in range(N):
        if dp[idx][cnt] == 0:
            continue
        char = S[idx]
        if char == "(":
            dp[idx + 1][cnt + 1] += dp[idx][cnt]
            dp[idx + 1][cnt + 1] %= MOD
        elif char == ")":
            if cnt > 0:
                dp[idx + 1][cnt - 1] += dp[idx][cnt]
                dp[idx + 1][cnt - 1] %= MOD
        else:
            dp[idx + 1][cnt + 1] += dp[idx][cnt]
            dp[idx + 1][cnt + 1] %= MOD
            if cnt > 0:
                dp[idx + 1][cnt - 1] += dp[idx][cnt]
                dp[idx + 1][cnt - 1] %= MOD

print(dp[N][0])
