from collections import defaultdict, deque

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

N = int(input())

graph = defaultdict(list)
for i in range(1, N + 1):
    l = list(map(int, input().split()))
    if len(l) == 1:
        continue
    _, *P = l
    graph[i].extend(P)

depth = bfs(graph, 1)
sorted_depth = topological_sort(graph)[::-1]

ans = list(filter(lambda x: x in depth and x != 1, sorted_depth))
print(" ".join(map(str, ans)))
