H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = []
def series(c, x, y, dx, dy):
    if c == 5:
        return True
    nx, ny = x + dx, y + dy
    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == "snuke"[c]:
        res = series(c + 1, nx, ny, dx, dy)
        if res:
            ans.append((nx, ny))
            return True
    return False

for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
                if series(1, i, j, dx, dy):
                    ans.append((i, j))

for x, y in ans[::-1]:
    print(x + 1, y + 1)