from sortedcontainers import SortedSet

N, K = map(int, input().split())
P = list(map(int, input().split()))

l = list(map(lambda x: x[0], sorted(enumerate(P), key=lambda x: x[1])))
s = SortedSet(l[:K])
mi = s[0]
ma = s[-1]
ans = ma - mi

for prev, cur in zip(l, l[K:]):
    s.remove(prev)
    s.add(cur)
    mi = s[0]
    ma = s[-1]
    ans = min(ans, ma - mi)

print(ans)
