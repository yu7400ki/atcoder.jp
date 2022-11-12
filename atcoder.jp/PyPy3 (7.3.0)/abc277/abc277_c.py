from collections import defaultdict, deque
from typing import List, Dict

Node  = int
Graph = Dict[Node, List[Node]]
Depth = Dict[Node, int]
Queue = List[Node]


def bfs(graph: Graph, n: Node) -> Depth:
    depth: Depth = defaultdict(lambda : -1)
    depth[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + 1

    return depth

N = int(input())

graph = defaultdict(list)

for _ in range(N):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


depth = bfs(graph, 1)

ans = max(depth.keys())

print(ans)
