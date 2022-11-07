from collections import defaultdict
from heapq import heappush, heappop
from typing import List, Tuple, Dict, Union


Node = int
Weight = int
Graph = Dict[Node, List[Tuple[Node, Weight]]]
Dist = Dict[Node, Union[Weight, float]]
Queue = List[Tuple[Weight, Node]]


def dijkstra(graph: Graph, start: Node) -> Dist:
    dist: Dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    queue: Queue = [(0, start)]
    while queue:
        d, u = heappop(queue)
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(queue, (dist[v], v))

    return dist


if __name__ == "__main__":
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    
    graph: Graph = defaultdict(list)
    rev: Graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        rev[b].append((a, c))

    dist = dijkstra(graph, 1)
    rev_dist = dijkstra(rev, 1)
    
    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, (T - dist[i] - rev_dist[i]) * A[i - 1])
    
    print(ans)
