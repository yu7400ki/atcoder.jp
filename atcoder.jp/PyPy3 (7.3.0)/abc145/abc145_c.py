from itertools import permutations

N = int(input())

xy = [()] * N
for i in range(N):
	xy[i] = tuple(map(int,input().split()))

def P(n,r):
	ans = 1
	for i in range(n,n-r,-1):
		ans *= i
	return ans

p = P(N,N)

distance = [0] * p
for i,way in enumerate(list(permutations(xy))):
	for j in range(N-1):
		distance[i] += ((way[j][0] - way[j+1][0]) ** 2 + (way[j][1] - way[j+1][1]) ** 2) ** 0.5

print(sum(distance) / p)