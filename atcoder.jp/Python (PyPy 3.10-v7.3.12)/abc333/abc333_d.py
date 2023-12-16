from collections import defaultdict, deque

def bfs(graph: defaultdict, n) -> defaultdict:
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

graph = defaultdict(set)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

if len(graph[1]) == 1:
    print(1)
    exit()

lst = []
for u in graph[1]:
    graph[u].remove(1)
    depth = bfs(graph, u)
    lst.append(len(depth))
    graph[u].add(1)

lst.sort()
lst.pop()
print(sum(lst) + 1)
