from heapq import heappush, heappop, heapify
from collections import Counter

N, Q = map(int, input().split())
A = list(map(int, input().split()))
count = Counter(A)
mex = [i for i in range(N+1) if i not in count]
heapify(mex)

for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1
    a = A[i]
    count[a] -= 1
    if count[a] == 0:
        heappush(mex, a)
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
    A[i] = x
    while mex[0] in count and count[mex[0]] > 0:
        heappop(mex)
    print(mex[0])
