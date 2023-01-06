from heapq import heapreplace, heapify

N, M = map(int, input().split())
A = list(map(lambda s: -int(s), input().split()))

heapify(A)
for _ in range(M):
    heapreplace(A, -(-A[0]//2))

print(-sum(A))
