from math import ceil
X, A, D, N = map(int,input().split())

if D == 0:
	print(abs(A-X))
	exit()

n = ceil(((X - A) / D) - 1)

if n <= 0:
	print(abs(A-X))
	exit()

if n >= N:
	print(abs((A+(N-1)*D)-X))
	exit()


ans = abs((A+(n-1)*D)-X)
if ans < abs((A+n*D)-X):
	print(ans)
else:
	print(abs((A+n*D)-X))
