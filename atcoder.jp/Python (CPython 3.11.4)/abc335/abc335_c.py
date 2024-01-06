from collections import deque

N, Q = map(int, input().split())

parts = [(i + 1, 0) for i in range(N)]
parts = deque(parts, N)

for _ in range(Q):
    t, u = input().split()
    if t == "1":
        dx = 1 if u == "R" else -1 if u == "L" else 0
        dy = 1 if u == "U" else -1 if u == "D" else 0
        head = parts[0]
        parts.appendleft((head[0] + dx, head[1] + dy))
    else:
        u = int(u) - 1
        print(parts[u][0], parts[u][1])
