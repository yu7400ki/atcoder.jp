from heapq import heappop, heappush, heapify

N, K = map(int,input().split())
P = list(map(int,input().split()))

heap_P = P[:K]
heapify(heap_P)
print(heap_P[0])
for i in range(K, N):
	heappush(heap_P, P[i])
	heappop(heap_P)
	print(heap_P[0])