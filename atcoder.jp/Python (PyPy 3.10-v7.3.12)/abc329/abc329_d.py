from heapq import heappush, heappop

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * (N + 1)
heap = []

for a in A:
    cnt[a] += 1
    heappush(heap, (-cnt[a], a))
    print(heap[0][1])
