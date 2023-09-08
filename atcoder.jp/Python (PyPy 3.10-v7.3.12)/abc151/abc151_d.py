import numpy as np

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
INF = np.inf

def grid_to_graph(grid, wall="#"):
    H, W = len(grid), len(grid[0])
    graph = [[0] * (W * H) for _ in range(W * H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == wall:
                continue
            parent = i * W + j
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < H and 0 <= y < W and grid[x][y] != wall:
                    adj = x * W + y
                    graph[parent][adj] = 1
                    graph[adj][parent] = 1
    return graph

def warshall_floyd(graph):
    V = len(graph)
    dist = [[graph[i][j] if graph[i][j] != 0 else 0 if i == j else INF for j in range(V)] for i in range(V)]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = grid_to_graph(S)
dist = warshall_floyd(graph)
ans = max([max(d, key=lambda x: -1 if x == INF else x) for d in dist])

print(ans)
