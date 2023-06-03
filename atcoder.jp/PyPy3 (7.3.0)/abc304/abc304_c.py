from collections import deque

def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def bfs(XY, n = 0, D = 0):
    ret = set()
    ret.add(n)
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for i, v in enumerate(XY):
            if i not in ret and dist(XY[u], v) <= D:
                queue.append(i)
                ret.add(i)

    return ret

N, D = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = bfs(XY, 0, D)

for i in range(N):
    if i in ans:
        print("Yes")
    else:
        print("No")
