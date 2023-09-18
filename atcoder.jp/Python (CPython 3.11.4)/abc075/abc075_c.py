from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parents = defaultdict(lambda: -1)
        self.rank = defaultdict(int)
        self.siz = defaultdict(lambda: 1)

    def find(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parents[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True

    def size(self, x) -> int:
        return self.siz[self.find(x)]

    def groups(self):
        return {x: self.siz[x] for x in self.parents if self.parents[x] == -1}

N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))

ans = 0
for i in range(M):
    uf = UnionFind()
    visited = set()
    for j in range(M):
        if i == j:
            continue
        a, b = edges[j]
        uf.union(a, b)
        visited.add(a)
        visited.add(b)
    if len(uf.groups()) > 1 or len(visited) < N:
        ans += 1

print(ans)
