from atcoder.dsu import DSU

N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))

ans = 0
for i in range(M):
    dsu = DSU(N)
    for j in range(M):
        if i == j:
            continue
        a, b = edges[j]
        dsu.merge(a, b)
    if len(dsu.groups()) > 1:
        ans += 1

print(ans)
