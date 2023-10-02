N, M, Q = map(int, input().split())

cnt = [[0] * N for _ in range(N)]
for _ in range(M):
    L, R = map(int, input().split())
    cnt[L - 1][R - 1] += 1

acc = [[0] * (N + 1) for _ in range(N + 1)]
for y in range(N):
    for x in range(N):
        acc[y + 1][x + 1] = acc[y][x + 1] + acc[y + 1][x] - acc[y][x] + cnt[y][x]

for _ in range(Q):
    p, q = map(int, input().split())
    br_x, br_y = q, q
    bl_x, bl_y = p, q
    tr_x, tr_y = q, p
    tl_x, tl_y = p, p
    ans = (
        acc[br_y][br_x]
        - acc[bl_y][bl_x - 1]
        - acc[tr_y - 1][tr_x]
        + acc[tl_y - 1][tl_x - 1]
    )
    print(ans)
