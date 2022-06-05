N = int(input())
p = list(map(int,input().split()))
p_set = set()

ans = [0] * N
for i in range(N):
	p_set.add(p[i])
	while ans[i] in p_set:
		ans[i] += 1
	print(ans[i])
