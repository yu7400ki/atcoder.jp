L = int(input())

def C(n,r):
	ans = 1
	for i in range(n,n-r,-1):
		ans *= i
	for i in range(2,r+1):
		ans //= i
	return ans

print(C(L-1,11))