from collections import defaultdict, deque

N, Q = map(int, input().split())

tree = defaultdict(list)
counter = defaultdict(int)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    counter[p] += x

def bfs(graph, n):
    depth = defaultdict(lambda: -1)
    depth[n] = counter[n]
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + counter[v]

    return depth

depth = bfs(tree, 1)

ans = [depth[i] for i in range(1, N+1)]

print(*ans)
