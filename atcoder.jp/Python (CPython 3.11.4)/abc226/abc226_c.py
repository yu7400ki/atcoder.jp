from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)
times = defaultdict(int)
for i in range(N):
    T, _, *A = map(int, input().split())
    graph[i+1].extend(A)
    times[i+1] = T

def bfs(graph: defaultdict, n) -> defaultdict:
    depth = defaultdict(lambda: -1)
    depth[n] = 0
    queue = deque()
    queue.append(n)
    ans = times[n]

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + 1
                ans += times[v]

    return ans

ans = bfs(graph, N)
print(ans)
