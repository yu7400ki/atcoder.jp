from collections import defaultdict

N = int(input())
SP = defaultdict(list)
for i in range(N):
	S, P = input().split()
	SP[S].append((i,int(P)))

SP_sorted = sorted(SP)
for S in SP_sorted:
	P = SP[S]
	for i,p in sorted(P, key=lambda p:p[1], reverse=True):
		print(i+1)