from collections import defaultdict, deque


def bfs(graph, n):
    depth = defaultdict(lambda: -1)
    depth[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + 1

    return depth


N_1, N_2, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth_1 = bfs(graph, 1)
depth_2 = bfs(graph, N_1 + N_2)

ans = max(depth_1.values()) + max(depth_2.values()) + 1
print(ans)
