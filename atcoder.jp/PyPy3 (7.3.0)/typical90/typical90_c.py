from collections import defaultdict, deque

def bfs(graph, n):
    depth = defaultdict(lambda : -1)
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


N = int(input())
graph = defaultdict(set)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

depth = bfs(graph, 1)
u = max(depth, key=lambda x: depth[x])
depth = bfs(graph, u)

print(max(depth.values()) + 1)
