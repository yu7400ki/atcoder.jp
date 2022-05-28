N, A, B = map(int,input().split())

a = list(range(A,N+1,A))
b = list(range(B,N+1,B))
c = list(range(A*B,N+1,A*B))

ans = (N * (1+N) // 2)
if len(a) != 0:
	ans -= len(a) * (A+a[-1]) // 2
if len(b) != 0:
	ans -= len(b) * (B+b[-1]) // 2
if len(c) != 0:
	ans += len(c) * (A*B+c[-1]) // 2


print(ans)