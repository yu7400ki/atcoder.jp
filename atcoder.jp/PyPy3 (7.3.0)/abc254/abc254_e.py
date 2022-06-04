from collections import defaultdict, deque

N, M = map(int,input().split())
graph = defaultdict(list)

for _ in range(M):
	a,b = map(int,input().split())
	graph[a].append(b)
	graph[b].append(a)

def bfs(n,limit):
	dic = defaultdict(lambda : -1)
	queue = deque()
	queue.append(n)
	dic[n] = 0
	for _ in range(limit):
		pos = queue.popleft()
		for i in graph[pos]:
			if dic[i] == -1:
				queue.append(i)
				dic[i] = dic[pos] + 1
	return dic

Q = int(input())
for _ in range(Q):
	x,k = map(int,input().split())
	dic = bfs(x,k)
	ans = 0
	for n in dic:
		ans += n
	print(ans)