from collections import defaultdict, deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

snuke = "snuke"

def is_ok(u, v):
    x, y = u
    nx, ny = v
    if not (0 <= nx < H and 0 <= ny < W):
        return False
    if S[x][y] not in snuke:
        return False
    if S[nx][ny] not in snuke:
        return False
    if (snuke.index(S[x][y]) + 1) % 5 != snuke.index(S[nx][ny]):
        return False
    return True

def bfs(x, y):
    depth = defaultdict(lambda : -1)
    depth[(x, y)] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        u = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = (u[0] + dx, u[1] + dy)
            if depth[v] == -1 and is_ok(u, v):
                queue.append(v)
                depth[v] = depth[u] + 1

    return depth

depth = bfs(0, 0)
if depth[(H - 1, W - 1)] != -1:
    print("Yes")
else:
    print("No")
