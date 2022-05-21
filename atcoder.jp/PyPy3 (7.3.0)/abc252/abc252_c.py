N = int(input())
S = [list(map(int,list(input()))) for _ in range(N)]

ans = float('INF')
for i in range(0,10):
	t = 0
	cnt = 0
	stop = []
	while cnt != N:
		for j in range(N):
			if j in stop:
				continue
			if S[j][t%10] == i:
				cnt += 1
				stop.append(j)
				break
		t += 1
	ans = min(t-1,ans)
print(ans)