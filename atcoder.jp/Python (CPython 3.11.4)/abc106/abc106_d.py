N, M, Q = map(int, input().split())

cnt = [[0] * N for _ in range(N)]
for _ in range(M):
    L, R = map(int, input().split())
    cnt[L-1][R-1] += 1

acc = [[0] * (N + 1) for _ in range(N + 1)]
for y in range(N):
    for x in range(N):
        acc[y+1][x+1] = acc[y][x+1] + acc[y+1][x] - acc[y][x] + cnt[y][x]

for _ in range(Q):
    p, q = map(int, input().split())
    ans = acc[q][q] - acc[p-1][q] - acc[q][p-1] + acc[p-1][p-1]
    print(ans)
