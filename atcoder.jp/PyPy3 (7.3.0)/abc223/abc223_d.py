from collections import defaultdict
from heapq import heappop, heappush, heapify

N, M = map(int,input().split())
graph = defaultdict(set)
memo = set(range(1,N+1))

for _ in range(M):
	a,b = map(int,input().split())
	graph[a].add(b)
	memo.discard(b)

memo = list(memo)
heapify(memo)

ans = []
while len(memo) != 0:
	i = heappop(memo)
	ans.append(i)
	l = graph[i]
	del graph[i]
	for j in l:
		for g in graph.values():
			if j in g:
				break
		else:
			heappush(memo, j)

if len(graph) == 0:
	print(*ans)
else:
	print(-1)