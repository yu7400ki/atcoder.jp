n = int(input())
t = list(map(int,input().split()))
A = [-100]

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
	flag = 1
	while True:
		if ctz(a) == t[i]:
			A.append(a)
			break
		else:
			if flag:
				a = 2**(t[i])
				while a <= A[-1]+1:
					a += 2**(t[i])
				flag = 0
			else:
				a += 2**(t[i])

print(A[-1])