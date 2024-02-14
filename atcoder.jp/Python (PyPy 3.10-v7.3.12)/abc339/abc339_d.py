from collections import defaultdict, deque
from functools import cache


class DefaultDict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def bfs(graph: defaultdict, n) -> defaultdict:
    depth = defaultdict(lambda: -1)
    depth[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + 1

    return depth


@cache
def default_factory(key):
    ret = []
    y1, x1, y2, x2 = key
    if (y1, x1) == (y2, x2):
        return ret
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny1, nx1 = y1 + dy, x1 + dx
        ny2, nx2 = y2 + dy, x2 + dx
        if ny1 < 0 or N <= ny1 or nx1 < 0 or N <= nx1 or S[ny1][nx1] == "#":
            ny1, nx1 = y1, x1
        if ny2 < 0 or N <= ny2 or nx2 < 0 or N <= nx2 or S[ny2][nx2] == "#":
            ny2, nx2 = y2, x2
        n = (ny1, nx1, ny2, nx2)
        if n != key:
            ret.append(n)
    return ret


N = int(input())
S = [list(input()) for _ in range(N)]

graph = DefaultDict(list)

p = []
for y in range(N):
    for x in range(N):
        if S[y][x] == "P":
            S[y][x] = "."
            p.append(y)
            p.append(x)
p = tuple(p)

graph = DefaultDict(default_factory)

depth = bfs(graph, p)
inf = 1 << 60
ans = inf
for p, d in depth.items():
    py1, px1, py2, px2 = p
    if (py1, px1) == (py2, px2):
        ans = min(ans, d)

print(ans if ans != inf else -1)
