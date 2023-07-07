H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

cntH = [[0] * W for _ in range(H)]
cntV = [[0] * W for _ in range(H)]

for y in range(H):
    tmp = 0
    for x in range(W):
        s = S[y][x]
        if s == ".":
            tmp += 1
        else:
            tmp = 0
        cntH[y][x] = tmp
    for x in range(W - 1, 0, -1):
        if cntH[y][x] == 0 or cntH[y][x - 1] == 0:
            continue
        else:
            cntH[y][x - 1] = cntH[y][x]

for x in range(W):
    tmp = 0
    for y in range(H):
        s = S[y][x]
        if s == ".":
            tmp += 1
        else:
            tmp = 0
        cntV[y][x] = tmp
    for y in range(H - 1, 0, -1):
        if cntV[y][x] == 0 or cntV[y - 1][x] == 0:
            continue
        else:
            cntV[y - 1][x] = cntV[y][x]

ans = 0
for y in range(H):
    for x in range(W):
        ans = max(ans, cntH[y][x] + cntV[y][x] - 1)

print(ans)
