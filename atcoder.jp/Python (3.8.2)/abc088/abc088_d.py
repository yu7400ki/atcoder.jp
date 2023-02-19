from collections import deque

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

def bfs(graph, start):
    queue = deque([start])
    dists = [-1] * len(graph)
    dists[start] = 0
    while queue:
        v = queue.popleft()
        for i, adj in enumerate(graph[v]):
            if adj == 0:
                continue
            if dists[i] != -1:
                continue
            dists[i] = dists[v] + 1
            queue.append(i)
    return dists

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

graph = grid_to_graph(grid)
dists = bfs(graph, 0)
dist = dists[-1]

if dist == -1:
    ans = -1
else:
    black = sum(row.count("#") for row in grid)
    white = H * W - black
    ans = white - dist - 1

print(ans)
