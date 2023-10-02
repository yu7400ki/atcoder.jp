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

Q = int(input())
for _ in range(Q):
    P = int(input())
    div = divisors(P)
    ans = -1
    for d in div:
        e = P // d
        d = min(d, N)
        e = min(e, N)
        for y in range(1 + d - 1, N + 1):
            for x in range(1 + e - 1, N + 1):
                tmp = acc[y][x] - acc[y - d][x] - acc[y][x - e] + acc[y - d][x - e]
                ans = max(ans, tmp)
    print(ans)
