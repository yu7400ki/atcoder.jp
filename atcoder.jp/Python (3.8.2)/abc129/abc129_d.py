H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

cntH = [[0] * W for _ in range(H)]
cntV = [[0] * W for _ in range(H)]

for y in range(H):
    tmp = 0
    for x in range(W):
        if S[y][x] == ".":
            tmp += 1
        else:
            tmp = 0
        cntH[y][x] = tmp
    for x in range(W - 1, 0, -1):
        if cntH[y][x - 1]:
            cntH[y][x - 1] = max(cntH[y][x - 1], cntH[y][x])

for x in range(W):
    tmp = 0
    for y in range(H):
        if S[y][x] == ".":
            tmp += 1
        else:
            tmp = 0
        cntV[y][x] = tmp
    for y in range(H - 1, 0, -1):
        if cntV[y - 1][x]:
            cntV[y - 1][x] = max(cntV[y - 1][x], cntV[y][x])

ans = 0
for i in range(H * W):
    y, x = divmod(i, W)
    ans = max(ans, cntH[y][x] + cntV[y][x] - 1)

print(ans)
