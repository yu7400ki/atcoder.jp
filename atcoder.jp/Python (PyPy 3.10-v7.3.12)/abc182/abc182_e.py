H, W, N, M = map(int, input().split())

HORIZONTAL = "-"
VERTICAL = "|"
BLOCK = "#"
LIGHT = "o"
EMPTY = "."

grid = [([BLOCK] + [EMPTY] * W + [BLOCK]) for _ in range(H)]
grid = [[BLOCK] * (W + 2)] + grid + [[BLOCK] * (W + 2)]

for _ in range(N):
    A, B = map(int, input().split())
    grid[A][B] = LIGHT

for _ in range(M):
    C, D = map(int, input().split())
    grid[C][D] = BLOCK

for y in range(1, H + 1):
    for x in range(1, W + 1):
        if grid[y][x] != LIGHT:
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x
            ny = y
            direction = ""
            if dx in (1, -1):
                direction = HORIZONTAL
            else:
                direction = VERTICAL
            while True:
                nx += dx
                ny += dy
                if grid[ny][nx] == EMPTY:
                    grid[ny][nx] = direction
                elif grid[ny][nx] in (BLOCK, LIGHT):
                    break
                elif grid[ny][nx] == direction:
                    break

ans = 0
for y in range(1, H + 1):
    for x in range(1, W + 1):
        if grid[y][x] in (HORIZONTAL, VERTICAL, LIGHT):
            ans += 1

print(ans)
