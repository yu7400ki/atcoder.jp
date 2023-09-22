N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

H = Q - P + 1
W = S - R + 1

ans = [["."] * W for _ in range(H)]

s1 = (A + max(-A, -B), B + max(-A, -B))
s2 = (A + max(1 - A, B - N) - 1, B - max(1 - A, B - N) - 1)

mt = P - 1
ml = R - 1
d1 = min(mt - s1[0], ml - s1[1])
d2 = min(mt - s2[0], ml + s2[1])

s1 = [s1[0] + d1 - mt, s1[1] + d1 - ml]
s2 = [s2[0] + d2 - mt, s2[1] - d2 - ml]

for i in range(max(H, W)):
    y = s1[0] + i
    x = s1[1] + i
    if 0 <= y < H and 0 <= x < W:
        ans[y][x] = "#"
    y = s2[0] + i
    x = s2[1] - i
    if 0 <= y < H and 0 <= x < W:
        ans[y][x] = "#"

for a in ans:
    print(*a, sep="")
