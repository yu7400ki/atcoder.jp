from math import gcd

N, A, B = map(int,input().split())

lcd = A*B // gcd(A,B)
ans = (N * (1+N) // 2)

if A <= N:
	a = list(range(A,N+1,A))
	ans -= len(a) * (A+a[-1]) // 2
if B <= N:
	b = list(range(B,N+1,B))
	ans -= len(b) * (B+b[-1]) // 2
if lcd <= N:
	c = list(range(lcd,N+1,lcd))
	ans += len(c) * (lcd + c[-1]) // 2

print(ans)