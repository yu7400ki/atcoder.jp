from atcoder.dsu import DSU

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edges[A].append(B)
uf = DSU(N)

cnt = 0
ans = [0] * N
for u in range(N - 1, -1, -1):
    ans[u] = cnt
    cnt += 1
    for v in edges[u]:
        if not uf.same(u, v):
            uf.merge(u, v)
            cnt -= 1

print(*ans, sep="\n")
