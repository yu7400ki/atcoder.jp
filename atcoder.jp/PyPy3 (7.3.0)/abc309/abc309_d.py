from collections import defaultdict, deque

N_1, N_2, M = map(int, input().split())

graph = defaultdict(set)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(graph, n):
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

    return depth

depth_1 = bfs(graph, 1)
depth_2 = bfs(graph, N_1 + N_2)

length_1 = max(depth_1.values())
length_2 = max(depth_2.values())

print(length_1 + length_2 + 1)
