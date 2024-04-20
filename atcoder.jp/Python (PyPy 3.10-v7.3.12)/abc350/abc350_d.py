from atcoder.dsu import DSU


def combination(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n - i + 1)
        denom = denom * i
    return numer // denom


N, M = map(int, input().split())
uf = DSU(N)

ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    uf.merge(a - 1, b - 1)

print(sum(combination(len(g), 2) for g in uf.groups()) - M)
