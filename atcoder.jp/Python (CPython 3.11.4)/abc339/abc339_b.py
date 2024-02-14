H, W, N = map(int, input().split())

g = [[False] * W for _ in range(H)]
pos = [0, 0]
dir = [0, -1]

for _ in range(N):
    if g[pos[1]][pos[0]]:
        dir = [dir[1], -dir[0]]
    else:
        dir = [-dir[1], dir[0]]
    g[pos[1]][pos[0]] = not g[pos[1]][pos[0]]
    pos[0] += dir[0]
    pos[1] += dir[1]
    pos[0] %= W
    pos[1] %= H

for i in range(H):
    print("".join(["#" if g[i][j] else "." for j in range(W)]))
