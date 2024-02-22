N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
x = int(N ** 0.5)

dp = [0] * N
dp[0] = 1
ep = [[0] * i for i in range(1, x + 1)]
for i in range(N):
    for d in range(1, x + 1):
        dp[i] += ep[d - 1][i % d]
        dp[i] %= MOD

    a = A[i]
    if a <= x:
        ep[a - 1][i % a] += dp[i]
        ep[a - 1][i % a] %= MOD
    else:
        for j in range(i + a, N, a):
            dp[j] += dp[i]
            dp[j] %= MOD

print(sum(dp) % MOD)
