from math import gcd

N, A, B = map(int,input().split())

lcd = A*B // gcd(A,B)
ans = (N * (1+N) // 2)

if A <= N:
	ans -= N//A * (A+A*(N//A)) // 2
if B <= N:
	ans -= N//B * (B+B*(N//B)) // 2
if lcd <= N:
	ans += N//lcd * (lcd + lcd*(N//lcd)) // 2

print(ans)