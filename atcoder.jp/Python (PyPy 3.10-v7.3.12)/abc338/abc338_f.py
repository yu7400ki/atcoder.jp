INF = 1 << 60

def warshall_floyd(graph):
    v = len(graph)
    dist = [[graph[i][j] if i != j else 0 for j in range(v)] for i in range(v)]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

N, M = map(int, input().split())

graph = [[INF] * N for _ in range(N)]
for _ in range(M):
    U, V, W = map(int, input().split())
    U -= 1
    V -= 1
    graph[U][V] = W

dist = warshall_floyd(graph)

dp = [[INF] * N for _ in range(1 << N)]
for i in range(N):
    dp[1 << i][i] = 0
for s in range(1, 1 << N):
    for v in range(N):
        if ~s >> v & 1: continue
        if dp[s][v] == INF: continue
        for u in range(N):
            if s >> u & 1: continue
            if dist[v][u] == INF: continue
            dp[s | 1 << u][u] = min(dp[s | 1 << u][u], dp[s][v] + dist[v][u])


ans = INF
for i in range(N):
    ans = min(ans, dp[(1 << N) - 1][i])

print(ans if ans != INF else "No")
