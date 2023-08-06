class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group(self):
        return len(self.roots())


N, M = map(int, input().split())
uf = UnionFind(N)

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.union(u, v)

root_pair = set()
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    root_pair.add((uf.find(x), uf.find(y)))

Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    p_root = uf.find(p)
    q_root = uf.find(q)
    if (p_root, q_root) in root_pair or (q_root, p_root) in root_pair:
        print("No")
    else:
        print("Yes")
