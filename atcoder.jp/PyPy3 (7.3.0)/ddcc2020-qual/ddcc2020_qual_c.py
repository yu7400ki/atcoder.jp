H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = [[0] * W for _ in range(H)]

s = 1
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            ans[i][j] = s
            s += 1

for i in range(H):
    for j in range(1, W):
        if ans[i][j] == 0:
            ans [i][j] = ans[i][j - 1]
    for j in range(W - 2, -1, -1):
        if ans[i][j] == 0:
            ans[i][j] = ans[i][j + 1]

for i in range(W):
    for j in range(1, H):
        if ans[j][i] == 0:
            ans[j][i] = ans[j - 1][i]
    for j in range(H - 2, -1, -1):
        if ans[j][i] == 0:
            ans[j][i] = ans[j + 1][i]

[print(*a) for a in ans]