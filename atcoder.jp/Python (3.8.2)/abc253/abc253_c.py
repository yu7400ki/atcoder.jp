from collections import defaultdict
import heapq

S_count = defaultdict(int)
min_x = []
max_x = []
Q = int(input())

for i in range(Q):
	query = list(map(int,input().split()))
	if query[0] == 1:
		heapq.heappush(min_x, query[1])
		heapq.heappush(max_x, -query[1])
		S_count[query[1]] += 1
	elif query[0] == 2:
		S_count[query[1]] -= min(query[2], S_count[query[1]])
	else:
		while S_count[(mi := heapq.heappop(min_x))] == 0:
			pass
		heapq.heappush(min_x, mi)
		while S_count[-(ma := heapq.heappop(max_x))] == 0:
			pass
		heapq.heappush(max_x, ma)
		print(-ma - mi)