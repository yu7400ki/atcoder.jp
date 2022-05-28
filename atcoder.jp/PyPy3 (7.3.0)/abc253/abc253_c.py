from collections import defaultdict

S_count = defaultdict(int)
min_x = float('INF')
max_x = -float('INF')
Q = int(input())

for i in range(Q):
	query = list(map(int,input().split()))
	if query[0] == 1:
		S_count[query[1]] += 1
	elif query[0] == 2:
		S_count[query[1]] -= min(query[2], S_count[query[1]])
		if S_count[query[1]] == 0:
			del S_count[query[1]]
	else:
		print(max(S_count) - min(S_count))