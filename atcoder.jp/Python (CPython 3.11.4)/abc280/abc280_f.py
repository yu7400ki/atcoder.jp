class PotentialUnionFind:
    def __init__(self, n: int):
        self.parents = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
        self.dif = [0] * n

    def find(self, x: int) -> int:
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            self.dif[x] += self.dif[self.parents[x]]
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
        return {x: self.siz[x] for x in self.parents if self.parents[x] == -1}


N, M, Q = map(int, input().split())
uf = PotentialUnionFind(N)
is_inf = [False] * N
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    if not uf.same(A, B):
        uf.union(A, B, C)
    elif uf.diff(A, B) != C:
        is_inf[uf.find(A)] = True

for _ in range(Q):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    if not uf.same(X, Y):
        print("nan")
    elif is_inf[uf.find(X)]:
        print("inf")
    else:
        print(uf.diff(X, Y))
