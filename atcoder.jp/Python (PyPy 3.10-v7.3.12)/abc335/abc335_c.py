from collections import deque

N, Q = map(int, input().split())

parts = [(i + 1, 0) for i in range(N)]
parts = deque(parts, N)

for _ in range(Q):
    t, u = input().split()
    match t:
        case "1":
            mov = (
                1 if u == "R" else -1 if u == "L" else 0,
                1 if u == "U" else -1 if u == "D" else 0,
            )
            head = parts[0]
            parts.appendleft((head[0] + mov[0], head[1] + mov[1]))
        case "2":
            u = int(u) - 1
            print(parts[u][0], parts[u][1])
