N = int(input())
p = list(map(int,input().split()))
p_set = set()

ans = [0] * (1+N)
for i in range(1,N+1):
	p_set.add(p[i-1])
	ans[i] = min(ans[i-1], p[i-1])
	while ans[i] in p_set:
		ans[i] += 1
	print(ans[i])