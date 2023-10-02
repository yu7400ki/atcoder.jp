def divisors(n):
    upper, lower = [], []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
    return lower + upper[::-1]


N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

acc = [[0] * (N + 1) for _ in range(N + 1)]
for y in range(N):
    for x in range(N):
        acc[y + 1][x + 1] = acc[y][x + 1] + acc[y + 1][x] - acc[y][x] + D[y][x]

ans = [-1] * (N**2 + 1)
ma = -1
for p in range(1, N**2 + 1):
    div = divisors(p)
    for d in div:
        e = p // d
        for y in range(1 + d - 1, N + 1):
            for x in range(1 + e - 1, N + 1):
                tmp = acc[y][x] - acc[y - d][x] - acc[y][x - e] + acc[y - d][x - e]
                ma = max(ma, tmp)
    ans[p - 1] = ma

Q = int(input())
for _ in range(Q):
    P = int(input())
    print(ans[P - 1])
