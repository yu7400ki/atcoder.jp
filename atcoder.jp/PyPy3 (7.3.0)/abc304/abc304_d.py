from bisect import bisect_left
from collections import defaultdict

W, H = map(int, input().split())
N = int(input())
pq = [tuple(map(int, input().split())) for _ in range(N)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

counts = defaultdict(int)
for p, q in pq:
    i = bisect_left(a, p)
    j = bisect_left(b, q)
    counts[(i, j)] += 1

max_count = max(counts.values())
min_count = 0

if len(counts) == (A + 1) * (B + 1):
    min_count = min(counts.values())
print(min_count, max_count)
