from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(set)
nodes = set()

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].add(B)
    graph[B].add(A)
    nodes.add(A)
    nodes.add(B)

def bfs(graph, n):
    x = 0
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
            else:
                if depth[v] != depth[u] - 1:
                    x += 1

    return depth, x // 2

ans = 0
while nodes:
    n = nodes.pop()
    depth, x = bfs(graph, n)
    nodes -= set(depth.keys())
    ans += x

print(ans)
