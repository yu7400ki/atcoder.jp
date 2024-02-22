N = int(input())

dx, dy = 1, 0
px, py = 0, 0
g = [["T"] * N for _ in range(N)]

for i in range(1, N**2):
    g[py][px] = i
    if (
        px + dx < 0
        or px + dx >= N
        or py + dy < 0
        or py + dy >= N
        or type(g[py + dy][px + dx]) == int
    ):
        dx, dy = -dy, dx
    px, py = px + dx, py + dy

for row in g:
    print(*row)
