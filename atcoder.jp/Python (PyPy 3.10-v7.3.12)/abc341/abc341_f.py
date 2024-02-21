from collections import defaultdict

N, M = map(int, input().split())
g = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
W = list(map(int, input().split()))
A = list(map(int, input().split()))

x = [1] * N
for u in sorted(range(N), key=lambda u: W[u]):
    dp = [0] * W[u]
    dp[0] = 1
    for v in g[u]:
        for i in range(W[u] - 1, W[v] - 1, -1):
            dp[i] = max(dp[i], dp[i - W[v]] + x[v])
    x[u] = max(dp)

print(sum(x[u] * A[u] for u in range(N)))
