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


N = int(input())
points = set()
uf = UnionFind()

for _ in range(N):
    point = tuple(map(int, input().split()))
    points.add(point)
    for dx, dy in ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)):
        neighbor = (point[0] + dx, point[1] + dy)
        if neighbor in points:
            uf.union(point, neighbor)

groups = uf.groups()
print(len(groups) + len(points.difference(uf.parents)))
