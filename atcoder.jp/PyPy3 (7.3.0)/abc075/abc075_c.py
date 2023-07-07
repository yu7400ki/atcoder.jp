from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(set)
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))
    graph[a].add(b)
    graph[b].add(a)

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

depth = bfs(graph, 1)
assert len(depth) == N

ans = 0
for a, b in edges:
    graph[a].discard(b)
    graph[b].discard(a)
    depth = bfs(graph, 1)
    ans += len(depth) != N
    graph[a].add(b)
    graph[b].add(a)

print(ans)
