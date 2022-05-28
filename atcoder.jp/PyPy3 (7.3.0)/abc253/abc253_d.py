N, A, B = map(int,input().split())

ans = (N * (1+N) // 2)

if A <= N:
	a = list(range(A,N+1,A))
	ans -= len(a) * (A+a[-1]) // 2
if B <= N:
	b = list(range(B,N+1,B))
	ans -= len(b) * (B+b[-1]) // 2
if A*B <= N:
	c = list(range(A*B,N+1,A*B))
	ans += len(c) * (A*B+c[-1]) // 2
	
print(ans)