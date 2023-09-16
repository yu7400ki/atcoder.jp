from collections import defaultdict, deque

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

uf = UnionFind()
points = [[None] * N for _ in range(N)]
graph = defaultdict(list)
ans = [None] * N

for _ in range(M):
    A, B, X, Y = map(int, input().split())
    A -= 1
    B -= 1
    if uf.union(A, B):
        graph[A].append(B)
        graph[B].append(A)
    points[A][B] = (X, Y)
    points[B][A] = (-X, -Y)

def bfs(graph: defaultdict, n) -> defaultdict:
    visited = [False] * N
    ans[n] = (0, 0)
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        if visited[u]:
            continue
        visited[u] = True
        for v in graph[u]:
            if ans[v] is None:
                queue.append(v)
                ans[v] = (ans[u][0] + points[u][v][0], ans[u][1] + points[u][v][1])

bfs(graph, 0)

for i in range(N):
    if ans[i] is None:
        print("undecidable")
    else:
        print(ans[i][0], ans[i][1])
