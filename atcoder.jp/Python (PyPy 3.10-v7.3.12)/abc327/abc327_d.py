from collections import defaultdict, deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(M):
    a = A[i]
    b = B[i]
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph: defaultdict, n) -> defaultdict:
    depth = defaultdict(lambda: -1)
    binary = defaultdict(lambda: -1)
    depth[n] = 0
    binary[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + 1
                binary[v] = 1 - binary[u]
            else:
                if binary[u] == binary[v]:
                    return None, False
                else:
                    continue

    return depth, True

nodes = set(range(1, N+1))
while nodes:
    n = nodes.pop()
    depth, is_bipartite = bfs(graph, n)
    if not is_bipartite:
        print("No")
        exit()
    else:
        nodes -= set(depth.keys())

print("Yes")
