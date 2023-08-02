from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)

def topological_sort(graph):
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

sorted_graph = topological_sort(graph)

count = [0] * N
for u in sorted_graph:
    for v in graph[u]:
        count[v] = max(count[v], count[u] + 1)

print(max(count))
