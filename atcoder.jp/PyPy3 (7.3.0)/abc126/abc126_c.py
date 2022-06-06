N, K = map(int,input().split())

ans = 0
for i in range(1,N+1):
	point = i
	percent = 1
	while point < K:
		point *= 2
		percent /= 2
	ans += percent / N

print(ans)