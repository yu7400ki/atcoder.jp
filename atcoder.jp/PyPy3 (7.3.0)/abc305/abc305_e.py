from collections import defaultdict, deque

N, M, K = map(int, input().split())

graph = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

sec = {}
for _ in range(K):
    p, h = map(int, input().split())
    sec[p] = h

secure = set()

def bfs(graph, n, d):
    depth = defaultdict(lambda : -1)
    depth[n] = 0
    queue = deque()
    queue.append(n)
    secure.add(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                if depth[u] >= d:
                    continue
                if sec.get(v) is not None and sec[v] >= d:
                    continue
                queue.append(v)
                depth[v] = depth[u] + 1
                sec[v] = depth[v]
                secure.add(v)

    return depth

sorted_sec = sorted(sec.items(), key=lambda x: x[1], reverse=True)

for k, h in sorted_sec:
    bfs(graph, k, h)

print(len(secure))
print(" ".join(map(str, sorted(secure))))
