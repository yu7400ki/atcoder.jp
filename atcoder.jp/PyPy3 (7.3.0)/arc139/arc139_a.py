n = int(input())
t = list(map(int,input().split()))
A = [-1]

def ctz(x):
	res = 0
	for i in range(1,x):
		if x % 2**i == 0:
			res += 1
		else:
			break
	return res

for i in range(n):
	a = max(2**(t[i]), A[-1]+1)
	while True:
		if ctz(a) == t[i]:
			A.append(a)
			break
		else:
			a += 1

print(A[-1])