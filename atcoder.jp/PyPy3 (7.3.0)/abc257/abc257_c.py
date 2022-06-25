N = int(input())
S = input()
W = list(map(int,input().split()))

def binary_search(ok,ng,func):
	while abs(ng - ok) > 1:
		mid = (ok+ng) // 2
		if func(mid):
			ok = mid
		else:
			ng = mid
	return ok

child = []
adult = []

for i in range(N):
	if S[i] == '0':
		child.append(W[i])
	else:
		adult.append(W[i])

if len(child) * len(adult) == 0:
	print(max(len(child), len(adult)))
	exit()

child.sort()
adult.sort()

ans = len(child) + len(adult) - (binary_search(-1, len(adult), lambda i: adult[i] <= child[-1]) + 1)
ans = max(ans, len(adult) + (binary_search(-1, len(child), lambda i: child[i] < adult[0]) + 1))

print(ans)
