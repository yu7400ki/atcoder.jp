import sys
sys.setrecursionlimit(10 ** 6)

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

snuke = "snuke"
def dfs(x, y, traversed = set()):
    traversed.add((x, y))
    if (x, y) == (H - 1, W - 1):
        return True
    flag = False
    c = S[x][y]
    if c not in snuke:
        return False
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if (nx, ny) in traversed:
            continue
        if S[nx][ny] not in snuke:
            continue
        if (snuke.index(c) + 1) % 5 == snuke.index(S[nx][ny]):
            flag |= dfs(nx, ny, traversed)
    return flag

if dfs(0, 0):
    print("Yes")
else:
    print("No")
