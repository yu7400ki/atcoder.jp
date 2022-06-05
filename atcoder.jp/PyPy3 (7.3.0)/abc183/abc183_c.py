from itertools import permutations

N, K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
for way in permutations(list(range(1,N))):
	time = T[0][way[0]]
	for i in range(N-2):
		time += T[way[i]][way[i+1]]
	time += T[way[N-2]][0]
	if time == K:
		cnt += 1

print(cnt)