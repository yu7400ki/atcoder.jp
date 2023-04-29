from collections import defaultdict

H, W = map(int, input().split())
C = defaultdict(lambda: defaultdict(lambda: False))
for i in range(H):
    c = list(input())
    for j in range(W):
        C[i][j] = c[j] == "#"

centers = []
for i in range(H):
    for j in range(W):
        if C[i][j]:
            if C[i + 1][j + 1] and C[i + 1][j - 1] and C[i - 1][j + 1] and C[i - 1][j - 1]:
                centers.append((i, j))

ans = [0] * min(H, W)
for y, x in centers:
    i = 1
    while C[y + i][x + i] and C[y + i][x - i] and C[y - i][x + i] and C[y - i][x - i]:
        i += 1
    ans[i - 2] += 1

print(" ".join(map(str, ans)))
