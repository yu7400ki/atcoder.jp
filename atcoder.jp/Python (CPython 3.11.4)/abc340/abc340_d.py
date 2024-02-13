from collections import defaultdict, deque

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
    g[x].append(i)

acc = [0] * N
for i in range(N - 1):
    acc[i + 1] = acc[i] + A[i]

inf = 1 << 60

q = deque([N - 1])
d = defaultdict(lambda: inf)
d[N - 1] = 0
while q:
    u = q.popleft()
    for v in g[u]:
        if d[v] == inf:
            q.append(v)
            d[v] = min(d[v], d[u] + B[v])

ans = float(inf)
for i in range(N):
    ans = min(ans, acc[i] + d[i])

print(ans)
