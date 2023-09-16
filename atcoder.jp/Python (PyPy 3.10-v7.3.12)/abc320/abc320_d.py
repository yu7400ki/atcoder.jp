from collections import defaultdict, deque

N, M = map(int, input().split())

points = [[None] * N for _ in range(N)]
graph = defaultdict(list)
ans = [None] * N

for _ in range(M):
    A, B, X, Y = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)
    points[A][B] = (X, Y)
    points[B][A] = (-X, -Y)

def bfs(graph: defaultdict, n) -> defaultdict:
    ans[n] = (0, 0)
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if ans[v] is None:
                queue.append(v)
                dx, dy = points[u][v]
                x, y = ans[u]
                ans[v] = (x + dx, y + dy)

bfs(graph, 0)

for i in range(N):
    if ans[i] is None:
        print("undecidable")
    else:
        print(ans[i][0], ans[i][1])
