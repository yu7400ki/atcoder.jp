class PotentialUnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [0] * n
        self.siz = [1] * n
        self.dif = [0] * n

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        else:
            root = self.find(self.parents[x])
            self.dif[x] += self.dif[self.parents[x]]
            self.parents[x] = root
            return self.parents[x]

    def weight(self, x: int) -> int:
        self.find(x)
        return self.dif[x]

    def diff(self, x: int, y: int) -> int:
        return self.weight(y) - self.weight(x)

    def union(self, x: int, y: int, w: int) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        w += self.weight(x)
        w -= self.weight(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
            w = -w
        self.parents[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        self.dif[ry] = w
        return True

    def same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x) -> int:
        return self.siz[self.find(x)]

    def groups(self):
        return {x: self.siz[x] for x in self.parents if self.parents[x] == x}


N, Q = map(int, input().split())

ans = []
uf = PotentialUnionFind(N)

for i in range(Q):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1

    if not uf.same(a, b):
        uf.union(a, b, d)
        ans.append(i + 1)
    else:
        if uf.diff(a, b) == d:
            ans.append(i + 1)

print(*ans, sep=" ")
