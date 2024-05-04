from atcoder.dsu import DSU
from typing import NamedTuple


class Edge(NamedTuple):
    u: int
    v: int
    w: int


N, M = map(int, input().split())
uf = DSU(N)
edges = []

for _ in range(M):
    K, C = map(int, input().split())
    A = list(map(int, input().split()))
    for a, b in zip(A, A[1:]):
        edges.append(Edge(a - 1, b - 1, C))
        uf.merge(a - 1, b - 1)

if len(uf.groups()) > 1:
    ans = -1
else:
    edges.sort(key=lambda x: x.w)
    uf = DSU(N)
    ans = 0
    for e in edges:
        if uf.same(e.u, e.v):
            continue
        uf.merge(e.u, e.v)
        ans += e.w

print(ans)
