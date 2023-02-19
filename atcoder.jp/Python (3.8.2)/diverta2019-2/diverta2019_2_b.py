from collections import Counter
from itertools import permutations

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(1)
    exit()

dists = []
for p in permutations(XY, 2):
    x1, y1 = p[0]
    x2, y2 = p[1]
    d = x2 - x1, y2 - y1
    dists.append(d)

c = Counter(dists)
ma = c.most_common(1)[0][1]

print(N - ma)
