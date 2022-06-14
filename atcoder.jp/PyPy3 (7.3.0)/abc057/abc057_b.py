from collections import defaultdict

N, M = map(int,input().split())
st = [tuple(map(int,input().split())) for _ in range(N)]
cp = [tuple(map(int,input().split())) for _ in range(M)]

dist = defaultdict(list)
for i in range(N):
    a, b = st[i]
    for j in range(M):
        c, d = cp[j]
        dist[i].append(abs(a-c) + abs(b-d))

for v in dist.values():
    t = float('inf')
    for i in range(M):
        d = v[i]
        if d < t:
            t = d
            ans = i + 1
    print(ans)