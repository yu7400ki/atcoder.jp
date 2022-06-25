from bisect import insort_left
from sys import stdin

def input():
	return stdin.readline().strip()

def binary_search(ok, ng, func):
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok


Q = int(input())
A = []
for _ in range(Q):
    query = list(map(int, input().split()))
    x = query[1]
    if query[0] == 1:
        insort_left(A, x)
        continue

    k = query[2] - 1
    if query[0] == 2:
        idx = binary_search(-1, len(A), lambda i: A[i] <= x)
        if idx - k < 0:
            print(-1)
        else:
            print(A[idx - k])

    elif query[0] == 3:
        idx = binary_search(len(A), -1, lambda i: A[i] >= x)
        if idx + k >= len(A):
            print(-1)
        else:
            print(A[idx + k])