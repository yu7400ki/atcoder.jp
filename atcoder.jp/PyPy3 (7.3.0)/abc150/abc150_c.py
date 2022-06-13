from itertools import permutations

N = int(input())
l = permutations(list(range(1,N+1)))
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

cnt = 1
for i in l:
	i = list(i)
	if i == P:
		a = cnt
	if i == Q:
		b = cnt
	cnt += 1

print(abs(a-b))