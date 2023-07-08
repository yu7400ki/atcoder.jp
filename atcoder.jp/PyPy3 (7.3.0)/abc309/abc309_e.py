from collections import defaultdict, deque

N, M = map(int, input().split())
P = list(map(int, input().split()))
XY = defaultdict(lambda : -1)
for _ in range(M):
    x, y = map(int, input().split())
    XY[x] = max(XY[x], y)

graph = defaultdict(set)

for i, p in enumerate(P):
    graph[p].add(i + 2)

def bfs(graph, n):
    ans = 0
    depth = defaultdict(lambda : -1)
    depth[n] = 0
    queue = deque()
    queue.append([n, XY[n]])
    ans += XY[n] >= 0

    while queue:
        u = queue.popleft()
        for v in graph[u[0]]:
            if depth[v] == -1:
                queue.append([v, max(u[1] - 1, XY[v])])
                depth[v] = depth[u[0]] + 1
                ans += queue[-1][1] >= 0

    return depth, ans

depth, ans = bfs(graph, 1)

print(ans)
