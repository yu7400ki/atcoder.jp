H, W, N = map(int, input().split())
T = list(input())
S = [list(input()) for _ in range(H)]

dx = {"L": -1, "R": 1, "U": 0, "D": 0}
dy = {"L": 0, "R": 0, "U": -1, "D": 1}

ans = 0
for y in range(H):
    for x in range(W):
        ny, nx = y, x
        if S[ny][nx] == "#":
            continue
        for t in T:
            ny += dy[t]
            nx += dx[t]
            if S[ny][nx] == "#":
                break
        else:
            ans += 1

print(ans)
