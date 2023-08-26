from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

S = None
G = None

for i in range(H):
    for j in range(W):
        if A[i][j] in [">", "<", "^", "v"]:
            if A[i][j] == ">":
                dx, dy = 1, 0
            elif A[i][j] == "<":
                dx, dy = -1, 0
            elif A[i][j] == "^":
                dx, dy = 0, -1
            else:
                dx, dy = 0, 1
            x, y = j, i
            while True:
                x += dx
                y += dy
                if x < 0 or x >= W or y < 0 or y >= H:
                    break
                if A[y][x] in [".", "!"]:
                    A[y][x] = "!"
                else:
                    break
        elif A[i][j] == "S":
            S = (j, i)
        elif A[i][j] == "G":
            G = (j, i)

depth = [[-1] * W for _ in range(H)]
depth[S[1]][S[0]] = 0
queue = deque([S])
while queue:
    x, y = queue.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue
        if depth[ny][nx] != -1:
            continue
        if A[ny][nx] not in [".", "G"]:
            continue
        depth[ny][nx] = depth[y][x] + 1
        queue.append((nx, ny))

if depth[G[1]][G[0]] == -1:
    print(-1)
else:
    print(depth[G[1]][G[0]])
