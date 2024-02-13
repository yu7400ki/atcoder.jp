from collections import defaultdict
from heapq import heappop, heappush

N = int(input())
A = []
B = []
X = []

g = defaultdict(list)

for i in range(N - 1):
    a, b, x = map(int, input().split())
    x -= 1
    A.append(a)
    B.append(b)
    X.append(x)
    g[i].append(x)

inf = 1 << 60

q = [(0, 0)]
d = [inf] * N
d[0] = 0
while q:
    dist, u = heappop(q)
    if d[u] < dist:
        continue
    for v in g[u]:
        if d[v] > d[u] + B[u]:
            d[v] = d[u] + B[u]
            heappush(q, (d[v], v))
    v = u + 1
    if v >= N:
        continue
    if d[v] > d[u] + A[u]:
        d[v] = d[u] + A[u]
        heappush(q, (d[v], v))

print(d[N - 1])
