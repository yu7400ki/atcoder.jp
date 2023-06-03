from bisect import bisect_left

W, H = map(int, input().split())
N = int(input())
pq = [tuple(map(int, input().split())) for _ in range(N)]
A = int(input())
a = sorted(list(map(int, input().split())))
B = int(input())
b = sorted(list(map(int, input().split())))

counts = [[0] * (A + 1) for _ in range(B + 1)]

filled = set()
min_count_tmp = float("inf")
min_count = 0
max_count = 0

for p, q in pq:
    i = bisect_left(a, p)
    j = bisect_left(b, q)
    counts[j][i] += 1
    filled.add((i, j))
    min_count_tmp = min(min_count_tmp, counts[j][i])
    if len(filled) == (A + 1) * (B + 1):
        min_count = min_count_tmp
    max_count = max(max_count, counts[j][i])

print(min_count, max_count)
