N, M = map(int,input().split())

par = list(range(N+1))

def merge(n):
	if par[n] == n:
		return n
	else:
		par[n] = merge(par[n])
		return par[n]

for _ in range(M):
	A, B = map(int,input().split())
	par[B] = par[A]
	merge(A)
	merge(B)

print(len(set(par))-2)