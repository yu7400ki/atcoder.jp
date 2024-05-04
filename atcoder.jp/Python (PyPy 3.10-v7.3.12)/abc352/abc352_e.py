from atcoder.dsu import DSU
from typing import NamedTuple


class Edge(NamedTuple):
    u: int
    v: int
    w: int


N, M = map(int, input().split())
edges = []
for _ in range(M):
    K, C = map(int, input().split())
    A = list(map(int, input().split()))
    for a, b in zip(A, A[1:]):
        edges.append(Edge(a - 1, b - 1, C))

edges.sort(key=lambda x: x.w)
uf = DSU(N)
ans = 0
for e in edges:
    if uf.same(e.u, e.v):
        continue
    uf.merge(e.u, e.v)
    ans += e.w

if len(uf.groups()) == 1:
    print(ans)
else:
    print(-1)
