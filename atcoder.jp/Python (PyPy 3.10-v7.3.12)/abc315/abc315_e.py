from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)
for i in range(1, N + 1):
    l = list(map(int, input().split()))
    if len(l) == 1:
        continue
    _, *P = l
    graph[i].extend(P)

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

depth = bfs(graph, 1)
ans = [k for k, v in depth.items() if v >= 1]

print(" ".join(map(str, sorted(ans))))
