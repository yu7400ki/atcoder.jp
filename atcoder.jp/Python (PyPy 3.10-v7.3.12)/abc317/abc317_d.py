def ceil(a, b):
    return (a + b - 1) // b

N = int(input())
X = []
Y = []
Z = []
for _ in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

inf = float("inf")
Z_sum = sum(Z)
dp = [[inf] * (Z_sum + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(Z_sum):
        if dp[i][j] == inf:
            continue
        if X[i] < Y[i]:
            a = ceil(Y[i] - X[i], 2)
            dp[i + 1][j + Z[i]] = min(dp[i + 1][j + Z[i]], dp[i][j] + a)
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        else:
            dp[i + 1][j + Z[i]] = min(dp[i + 1][j + Z[i]], dp[i][j])

z = ceil(Z_sum, 2)
print(min(dp[-1][z:]))
