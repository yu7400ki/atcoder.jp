from collections import defaultdict

N, K, P = map(int, input().split())
C = []
A = []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

inf = 1 << 60
dp = [defaultdict(lambda: inf) for _ in range(N + 1)]
dp[0][(0,) * K] = 0

for i in range(N):
    for param, cost in dp[i].items():
        tmp = list(param)
        for j in range(K):
            tmp[j] += A[i][j]
            tmp[j] = min(tmp[j], P)
        tmp = tuple(tmp)
        dp[i + 1][tmp] = min(dp[i + 1][tmp], cost + C[i])
        dp[i + 1][param] = min(dp[i + 1][param], cost)

if dp[N][(P,) * K] == inf:
    print(-1)
else:
    print(dp[N][(P,) * K])
