from collections import defaultdict

N = int(input())
ans = defaultdict(lambda : 0)

def g(x,y,z):
	return x**2 + y**2 + z**2 + x*y + y*z + z*x

limit = int(N**0.5)+1
for x in range(1,limit):
	for y in range(1,limit):
		for z in range(1,limit):
			a = g(x,y,z)
			if a <= N:
				ans[a] += 1

for i in range(1,N+1):
	if i in ans:
		print(ans[i])
	else:
		print(0)