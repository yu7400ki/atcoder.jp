from collections import defaultdict


def topological_sort(graph: defaultdict) -> list:
    indegree = defaultdict(int)
    for k, v in graph.items():
        for w in v:
            indegree[w] += 1
        if k not in indegree:
            indegree[k] = 0
    res = []
    stack = []
    for k, v in indegree.items():
        if v == 0:
            stack.append(k)
    while stack:
        v = stack.pop()
        res.append(v)
        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                stack.append(w)
    return res


N, M = map(int, input().split())
graph = defaultdict(list)
cost = defaultdict(int)
beautiful = defaultdict(int)
for _ in range(M):
    u, v, b, c = map(int, input().split())
    graph[u].append(v)
    cost[(u, v)] = c
    beautiful[(u, v)] = b

res = topological_sort(graph)

inf = 1 << 60
ans = [(inf, 0) for _ in range(N + 1)]
ans[1] = (0, 0)

for u in res:
    for v in graph[u]:
        new = (ans[u][0] + cost[(u, v)], ans[u][1] + beautiful[(u, v)])
        ans[v] = max(
            ans[v],
            new,
            key=lambda x: x[1] / x[0],
        )

print(ans[N][1] / ans[N][0])
