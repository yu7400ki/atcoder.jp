from bisect import bisect_left
from collections import defaultdict

W, H = map(int, input().split())
N = int(input())
pq = [tuple(map(int, input().split())) for _ in range(N)]
A = int(input())
a = sorted(list(map(int, input().split())))
B = int(input())
b = sorted(list(map(int, input().split())))

# counts = [[0] * (A + 1) for _ in range(B + 1)]
counts = defaultdict(lambda: defaultdict(int))

filled = set()
min_count = float("inf")
max_count = 0

for p, q in pq:
    i = bisect_left(a, p)
    j = bisect_left(b, q)
    counts[j][i] += 1
    filled.add((i, j))
    min_count = min(min_count, counts[j][i])
    max_count = max(max_count, counts[j][i])

if len(filled) == (A + 1) * (B + 1):
    print(min_count, max_count)
else:
    print(0, max_count)
