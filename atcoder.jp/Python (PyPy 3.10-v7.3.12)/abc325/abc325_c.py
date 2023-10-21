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

H, W = map(int, input().split())
S = [list("." + input() + ".") for _ in range(H)]
S = [["."] * (W + 2)] + S + [["."] * (W + 2)]

uf = UnionFind()
solo = 0
for y in range(1, H + 1):
    for x in range(1, W + 1):
        if S[y][x] == ".":
            continue
        is_solo = True
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == dx == 0:
                    continue
                if S[y + dy][x + dx] == "#":
                    uf.union((y, x), (y + dy, x + dx))
                    is_solo = False
        solo += is_solo

ans = len(uf.groups()) + solo
print(ans)
