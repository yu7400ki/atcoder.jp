from collections import defaultdict, deque

def bfs(graph, n, a):
    depth = defaultdict(lambda : [-1, -1])
    depth[n][0] = 0
    depth[n][1] = a[n]
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v][0] == -1:
                queue.append(v)
                depth[v][0] = depth[u][0] + 1
                depth[v][1] = depth[u][1] + a[v]
            elif depth[v][0] == depth[u][0] + 1:
                depth[v][1] = max(depth[v][1], depth[u][1] + a[v])

    return depth

N = int(input())
A = list(map(int, input().split()))
graph = defaultdict(set)

for i in range(N):
    S = list(input())
    for j in range(N):
        if S[j] == "Y":
            graph[i].add(j)

Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    U -= 1
    V -= 1

    depth = bfs(graph, U, A)
    d, v = depth[V]
    if d == -1:
        print("Impossible")
    else:
        print(d, v)
