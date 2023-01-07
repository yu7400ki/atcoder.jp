from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())

graph = defaultdict(set)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

ans = 1
limit = 10 ** 6

def dfs(graph, n, visited):
    global ans
    visited.add(n)
    for v in graph[n]:
        if v not in visited:
            ans += 1
            if ans >= limit:
                print(limit)
                exit()
            dfs(graph, v, visited)
    visited.discard(n)

dfs(graph, 1, set())

print(ans)
