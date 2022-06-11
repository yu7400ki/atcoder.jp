from collections import defaultdict

N, K = map(int,input().split())
A = list(map(int,input().split()))
XY = [tuple(map(int,input().split())) for _ in range(N)]

dist = defaultdict(lambda : float('inf'))
for i in A:
	i -= 1
	xy1 = XY[i]
	for j in range(N):
		if j+1 in A:
			continue
		xy2 = XY[j]
		d = (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2
		dist[XY[j]] = min(dist[XY[j]], d)

ans = 0
for d in dist.values():
	ans = max(ans, d)

print(ans**0.5)