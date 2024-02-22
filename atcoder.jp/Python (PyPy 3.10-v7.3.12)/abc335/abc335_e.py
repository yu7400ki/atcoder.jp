from collections import defaultdict
from atcoder.dsu import DSU

N, M = map(int, input().split())
A = list(map(int, input().split()))
g = defaultdict(list)
uf = DSU(N)
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if A[u] == A[v]:
        uf.merge(u, v)
    else:
        if A[u] > A[v]:
            u, v = v, u
        g[u].append(v)

dp = [-1] * N
dp[0] = 1
for i in sorted(range(N), key=lambda x: A[x]):
    u = uf.leader(i)
    if dp[u] == -1:
        continue
    for j in g[u]:
        v = uf.leader(j)
        if u == v:
            continue
        dp[v] = max(dp[v], dp[u] + 1)

print(max(dp[N - 1], 0))
