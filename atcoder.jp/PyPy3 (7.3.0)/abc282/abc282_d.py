from collections import defaultdict, deque

def bipartite(graph):
    color = defaultdict(lambda : 0)
    color[1] = 1
    queue = deque()
    queue.append(1)

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
color = bipartite(graph)

if color is None:
    print(ans)
    exit()

u = set()
v = set()
for i, j in color.items():
    if j == 1:
        u.add(i)
    else:
        v.add(i)


for i in range(1, N+1):
    if i in u:
        ans += len(v) - len(graph[i] & v)
    elif i in v:
        ans += len(u) - len(graph[i] & u)



print(ans // 2)