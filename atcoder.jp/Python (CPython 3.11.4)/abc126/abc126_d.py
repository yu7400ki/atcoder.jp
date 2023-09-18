from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

def bfs(graph: defaultdict, n) -> defaultdict:
    depth = defaultdict(lambda: -1)
    depth[n] = 0
    queue = deque()
    queue.append(n)
    ans = [0] * N

    while queue:
        u = queue.popleft()
        for (v, w) in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + 1
                if w % 2 == 0:
                    ans[v] = ans[u]
                else:
                    ans[v] = 1 - ans[u]

    return ans

ans = bfs(graph, 0)
for i in range(N):
    print(ans[i])
