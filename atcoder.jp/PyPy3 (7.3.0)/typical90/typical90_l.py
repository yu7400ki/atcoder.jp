from collections import defaultdict

class UnionFind():
    def __init__(self):
        self.par = defaultdict(lambda: -1)
        self.rank = defaultdict(lambda: 0)
        self.size = defaultdict(lambda: 1)

    def find(self, node):
        if self.par[node] == -1:
            return node
        self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        if self.rank[u] < self.rank[v]:
            u, v = v, u
        self.par[v] = u
        if self.rank[u] == self.rank[v]:
            self.rank[u] += 1
        self.size[u] += self.size[v]
        return True

    def same(self, u, v):
        return self.find(u) == self.find(v)

H, W = map(int, input().split())

Q = int(input())
uf = UnionFind()
seen = set()
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        rc = (q[1], q[2])
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nrc = (rc[0] + dr, rc[1] + dc)
            if nrc in seen:
                uf.union(rc, nrc)
        seen.add(rc)
    else:
        rca = (q[1], q[2])
        rcb = (q[3], q[4])
        if rca not in seen or rcb not in seen:
            print('No')
            continue
        if uf.same(rca, rcb):
            print('Yes')
        else:
            print('No')
