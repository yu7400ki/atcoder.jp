from collections import defaultdict, deque

N = int(input())

graph = defaultdict(set)
nodes = set()
for _ in range(N):
    S, T = input().split()
    graph[S].add(T)
    nodes.add(S)


def hasCycle(graph, node):
    depth = defaultdict(lambda: -1)
    depth[node] = 0
    queue = deque([node])
    res = False
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                queue.append(u)
            else:
                res = True
    return depth, res


while nodes:
    node = nodes.pop()
    depth, res = hasCycle(graph, node)
    if res:
        print("No")
        exit()
    for k, v in depth.items():
        nodes.discard(k)

print("Yes")
