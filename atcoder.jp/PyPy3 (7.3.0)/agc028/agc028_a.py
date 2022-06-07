from math import gcd

N, M = map(int,input().split())
S = input()
T = input()

g = gcd(N,M)
L = N * M // g

n = N//g
m = M//g

for i in range(g):
	if S[i*n] != T[i*m]:
		print(-1)
		exit()

print(L)