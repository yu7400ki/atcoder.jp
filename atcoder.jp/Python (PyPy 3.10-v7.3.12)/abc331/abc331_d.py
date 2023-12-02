N, Q = map(int, input().split())
P = [list(map(lambda s: s == "B", input())) for _ in range(N)]

acc = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        acc[i + 1][j + 1] = acc[i + 1][j] + acc[i][j + 1] - acc[i][j] + P[i][j]

for _ in range(Q):
    y1, x1, y2, x2 = map(int, input().split())
    lu = (
        acc[y1 % N][x1 % N]
        + (y1 // N) * acc[N][x1 % N]
        + (x1 // N) * acc[y1 % N][N]
        + (y1 // N) * (x1 // N) * acc[N][N]
    )
    ru = (
        acc[y1 % N][x2 % N + 1]
        + (y1 // N) * acc[N][x2 % N + 1]
        + (x2 // N) * acc[y1 % N][N]
        + (y1 // N) * (x2 // N) * acc[N][N]
    )
    ld = (
        acc[y2 % N + 1][x1 % N]
        + (y2 // N) * acc[N][x1 % N]
        + (x1 // N) * acc[y2 % N + 1][N]
        + (y2 // N) * (x1 // N) * acc[N][N]
    )
    rd = (
        acc[y2 % N + 1][x2 % N + 1]
        + (y2 // N) * acc[N][x2 % N + 1]
        + (x2 // N) * acc[y2 % N + 1][N]
        + (y2 // N) * (x2 // N) * acc[N][N]
    )
    ans = rd - ru - ld + lu
    print(ans)
