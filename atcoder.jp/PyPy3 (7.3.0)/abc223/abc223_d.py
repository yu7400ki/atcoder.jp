from collections import defaultdict
from heapq import heappop, heappush, heapify

N, M = map(int,input().split())
graph = defaultdict(set)
graph_memo = defaultdict(set)
memo = set(range(1,N+1))

for _ in range(M):
	a,b = map(int,input().split())
	graph[a].add(b)
	graph_memo[b].add(a)
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
		graph_memo[j].discard(i)
		if len(graph_memo[j]) == 0:
			heappush(memo, j)

if len(graph) == 0:
	print(*ans)
else:
	print(-1)