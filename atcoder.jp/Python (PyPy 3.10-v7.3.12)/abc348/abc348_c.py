from heapq import heappush
from collections import defaultdict

N = int(input())
d = defaultdict(list)
for _ in range(N):
    A, C = map(int, input().split())
    heappush(d[C], A)
ans = max(d.values(), key=lambda x: x[0])
print(ans[0])
