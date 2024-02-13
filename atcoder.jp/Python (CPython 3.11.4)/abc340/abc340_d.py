from collections import defaultdict
from heapq import heappop, heappush

N = int(input())

g = defaultdict(list)

for i in range(N - 1):
    a, b, x = map(int, input().split())
    x -= 1
    g[i].append([i + 1, a])
    g[i].append([x, b])

inf = 1 << 60

q = [(0, 0)]
d = [inf] * N
d[0] = 0
while q:
    u, dist = heappop(q)
    if d[u] < dist:
        continue
    for v in g[u]:
        if d[v[0]] > d[u] + v[1]:
            d[v[0]] = d[u] + v[1]
            heappush(q, (v[0], d[v[0]]))

print(d[N - 1])
