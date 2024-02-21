from collections import defaultdict, deque
import numpy as np


class DefaultDict(defaultdict):
    def __missing__(self, key):
        ret = self[key] = self.default_factory(key)
        return ret


def bfs(graph: defaultdict, n, max_depth: int = 10) -> defaultdict:
    depth = defaultdict(lambda: -1)
    depth[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        if depth[u] == max_depth:
            break
        for v in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + 1

    return depth


H, W = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]

s = np.array(S, dtype=np.int8)
g = np.array([i for i in range(1, H * W + 1)], dtype=np.int8).reshape(H, W)
nh, nw = H - 1, W - 1


def default_factory(key: bytes):
    arr = np.frombuffer(key, dtype=np.int8).reshape(H, W)
    ret = []
    for i in range(4):
        cp = arr.copy()
        x, y = i & 1, i >> 1
        ny = y + nh
        nx = x + nw
        cp[y:ny, x:nx] = np.rot90(cp[y:ny, x:nx], k=2)
        ret.append(cp.tobytes())
    return ret


graph = DefaultDict(default_factory)
depth_from_start = bfs(graph, s.tobytes())
depth_from_goal = bfs(graph, g.tobytes())

ans = float("inf")
for k, v in depth_from_start.items():
    if depth_from_goal[k] != -1:
        ans = min(ans, v + depth_from_goal[k])

print(ans if ans != float("inf") else -1)
