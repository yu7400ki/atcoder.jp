from itertools import permutations

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

dists = set()
for p in permutations(XY, 2):
    x1, y1 = p[0]
    x2, y2 = p[1]
    d = x2 - x1, y2 - y1
    dists.add(d)

ans = 1 << 60
for dx, dy in dists:
    tmp = 1
    current = XY[0]
    rest = set(XY[1:])
    while rest:
        x1, y1 = current
        x2, y2 = x1 + dx, y1 + dy
        if (x2, y2) in rest:
            rest.remove((x2, y2))
            current = x2, y2
        else:
            tmp += 1
            current = rest.pop()
    ans = min(ans, tmp)

print(ans)
