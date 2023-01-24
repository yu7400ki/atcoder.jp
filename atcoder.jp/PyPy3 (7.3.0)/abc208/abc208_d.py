N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    graph[A][B] = C

INF = 1 << 60

def warshall_floyd(graph, K):
    dist = [[graph[i][j] if graph[i][j] != 0 else 0 if i == j else INF for j in range(N)] for i in range(N)]

    for k in range(K + 1):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


ans = 0
for k in range(N):
    dist = warshall_floyd(graph, k)
    for i in range(N):
        for j in range(N):
            if dist[i][j] == INF:
                continue
            ans += dist[i][j]

print(ans)
