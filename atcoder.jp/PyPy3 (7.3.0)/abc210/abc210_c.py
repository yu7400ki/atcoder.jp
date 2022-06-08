from collections import deque

N, K = map(int,input().split())
c = list(map(int,input().split()))

choose = deque(c[:K])
ans = len(set(choose))

for i in range(K, N):
	choose.popleft()
	choose.append(c[i])
	ans = max(ans, len(set(choose)))

print(ans)