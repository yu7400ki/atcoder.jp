from collections import defaultdict

S_count = defaultdict(int)
min_x = float('INF')
max_x = -float('INF')
Q = int(input())

for i in range(Q):
	query = list(map(int,input().split()))
	if query[0] == 1:
		min_x = min(min_x, query[1])
		max_x = max(max_x, query[1])
		S_count[query[1]] += 1
	elif query[0] == 2:
		S_count[query[1]] -= min(query[2], S_count[query[1]])
		if S_count[query[1]] == 0:
			if query[1] == min_x:
				del S_count[query[1]]
				min_x = min(S_count)
			elif query[1] == max_x:
				del S_count[query[1]]
				max_x = max(S_count)
			else:
				del S_count[query[1]]
	else:
		print(max_x - min_x)