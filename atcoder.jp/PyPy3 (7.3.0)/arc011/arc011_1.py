m, n, N = map(int,input().split())

ans = N
while N >= m:
	a = N // m * n
	ans += a
	N %= m
	N += a

print(ans)