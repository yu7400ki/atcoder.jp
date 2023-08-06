from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

if graph[1] & graph[N]:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
