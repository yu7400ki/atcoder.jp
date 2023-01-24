N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a-1][b-1] = t
    graph[b-1][a-1] = t

INF = 1 << 60

def warshall_floyd(graph):
    dist = [[graph[i][j] if graph[i][j] != 0 else 0 if i == j else INF for j in range(N)] for i in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

dist = warshall_floyd(graph)

ans = min([max(d) for d in dist])

print(ans)
