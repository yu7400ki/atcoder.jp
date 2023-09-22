from itertools import permutations
import math


N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

s = 0
perm = list(permutations(range(N)))
for p in perm:
    for i in range(N - 1):
        x1, y1 = xy[p[i]]
        x2, y2 = xy[p[i + 1]]
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        s += d


print(s / len(perm))
