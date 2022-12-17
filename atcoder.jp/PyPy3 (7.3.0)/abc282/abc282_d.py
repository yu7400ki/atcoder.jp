from collections import defaultdict, deque


def bipartite(graph, n):
    color = defaultdict(lambda: 0)
    color[n] = 1
    queue = deque()
    queue.append(n)

    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if color[u] == 0:
                color[u] = -color[v]
                queue.append(u)
            elif color[u] == color[v]:
                return None

    return color


N, M = map(int, input().split())

graph = defaultdict(set)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

ans = 0

nodes = set(range(1, N+1))
colors = []
while nodes:
    color = bipartite(graph, nodes.pop())
    if color is None:
        print(ans)
        exit()
    colors.append(color)
    nodes = nodes.difference(set(color.keys()))

for color in colors:
    _ans = 0
    u = set()
    v = set()
    for i, j in color.items():
        if j == 1:
            u.add(i)
        else:
            v.add(i)

    for i in range(1, N+1):
        if i in u:
            _ans += len(v) - len(graph[i] & v)
        elif i in v:
            _ans += len(u) - len(graph[i] & u)

    _ans //= 2
    ans += _ans


print(ans)
