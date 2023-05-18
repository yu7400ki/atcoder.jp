H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

count_x = [0] * W
count_y = [0] * H

for y in range(H):
    for x in range(W):
        count_x[x] += grid[y][x]
        count_y[y] += grid[y][x]

ans = [[0] * W for _ in range(H)]

for y in range(H):
    for x in range(W):
        ans[y][x] = count_x[x] + count_y[y] - grid[y][x]
    print(" ".join(map(str, ans[y])))
