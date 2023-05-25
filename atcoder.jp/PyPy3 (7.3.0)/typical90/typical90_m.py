from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        d, u = heappop(queue)
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(queue, (dist[v], v))

    return dist

N, M = map(int, input().split())
graph = defaultdict(set)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].add((b, c))
    graph[b].add((a, c))

dist_from_1 = dijkstra(graph, 1)
dist_from_N = dijkstra(graph, N)

for k in range(1, N + 1):
    print(dist_from_1[k] + dist_from_N[k])
