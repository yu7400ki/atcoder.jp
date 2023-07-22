import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

def search(x, y, visited = set(), stop = set()):
    if S[y][x] == "#":
        return
    if (x, y) in stop:
        return
    visited.add((x, y))
    stop.add((x, y))
    ix, iy = x, y
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        x, y = ix, iy
        if S[y+dy][x+dx] == "#":
            continue
        while S[y+dy][x+dx] != "#":
            x += dx
            y += dy
            visited.add((x, y))
        visited.add((x, y))
        search(x, y)
    return len(visited)

ans = search(1, 1)
print(ans)
