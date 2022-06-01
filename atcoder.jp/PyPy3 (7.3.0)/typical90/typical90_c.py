from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
	a,b = map(int,input().split())
	graph[a].append(b)
	graph[b].append(a)

def bfs(n):
	dic = defaultdict(lambda : -1)
	m = 0
	queue = deque()
	queue.append(n)
	dic[n] = 0
	while len(queue) != 0:
		pos = queue.popleft()
		for i in graph[pos]:
			if dic[i] == -1:
				queue.append(i)
				dic[i] = dic[pos] + 1
				if dic[pos] + 1 > m:
					ans = i
	return ans,dic

m = bfs(1)[0]
n = bfs(m)
print(n[1][n[0]]+1)
