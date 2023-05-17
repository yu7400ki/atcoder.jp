class UnionFind():
    def __init__(self, nodes):
        self.nodes = nodes
        self.par = {}
        self.rank = {}
        self.size = {}
        for node in nodes:
            self.par[node] = -1
            self.rank[node] = 0
            self.size[node] = 1

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


N, Q = map(int, input().split())

uf = UnionFind(range(N))

for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 0:
        uf.union(u, v)
    else:
        print(1 if uf.same(u, v) else 0)
