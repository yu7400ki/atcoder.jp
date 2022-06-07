from math import gcd

N, M = map(int,input().split())
S = input()
T = input()

g = gcd(N,M)
L = N * M // g
X = [''] * L

for i in range(N):
	X[i*(L//N)] = S[i]

for j in range(M):
	if X[j*(L//M)] != '':
		if X[j*L//M] == T[j]:
			continue
		else:
			print(-1)
			exit()
	else:
		X[j*(L//M)] = T[j]

print(L)