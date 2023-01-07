from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(set)
nodes = set([i for i in range(1, N + 1)])

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


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

ans = 0

while nodes:
    root = nodes.pop()
    depth = bfs(graph, root)

    for key, value in depth.items():
        nodes.discard(key)

    ans += 1

print(ans)
