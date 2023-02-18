H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]

INF = 1 << 60
def warshall_floyd(graph):
    V = len(graph)
    dist = [[graph[i][j] if graph[i][j] != 0 else 0 if i == j else INF for j in range(V)] for i in range(V)]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

dist = warshall_floyd(C)

ans = 0
for x in range(H):
    for y in range(W):
        n = A[x][y]
        if n != -1:
            ans += dist[n][1]

print(ans)
