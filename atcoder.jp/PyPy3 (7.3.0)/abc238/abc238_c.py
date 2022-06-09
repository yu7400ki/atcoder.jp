N = int(input())
MOD = 998244353

ans = 0
i = 1
while True:
	mi = min(10**i-1, N)
	K = mi-10**(i-1)+1
	ans += K*(1+K)//2
	ans %= MOD
	i += 1
	if mi == N:
		break

print(ans)