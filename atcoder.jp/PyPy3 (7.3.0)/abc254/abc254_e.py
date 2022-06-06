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
	ans = n
	while len(queue) != 0:
		pos = queue.popleft()
		for i in graph[pos]:
			if dic[i] == -1:
				dic[i] = dic[pos] + 1
				if dic[i] <= limit:
					ans += i
					if dic[i] < limit:
						queue.append(i)
	return ans

Q = int(input())
for _ in range(Q):
	x,k = map(int,input().split())
	ans = bfs(x,k)
	print(ans)
