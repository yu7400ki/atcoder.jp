from collections import defaultdict, deque

N_1, N_2, M = map(int, input().split())

graph = defaultdict(set)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(graph, n):
    queue = deque([n])
    depth = {n: 0}
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in depth:
                depth[w] = depth[v] + 1
                queue.append(w)
    return depth

depth_1 = bfs(graph, 1)
depth_2 = bfs(graph, N_1 + N_2)

length_1 = max(depth_1.values())
length_2 = max(depth_2.values())

print(length_1 + length_2 + 1)
