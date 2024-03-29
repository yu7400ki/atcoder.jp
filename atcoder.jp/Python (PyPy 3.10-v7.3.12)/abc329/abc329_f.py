N, Q = map(int, input().split())
C = list(map(int, input().split()))

c = [set([c]) for c in C]
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if len(c[a]) < len(c[b]):
        c[b] |= c[a]
        c[a] = set()
    else:
        c[a] |= c[b]
        c[b] = c[a]
        c[a] = set()
    print(len(c[b]))
