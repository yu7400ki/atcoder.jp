N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

a = max(A)
for i in range(len(A)):
	if A[i] == a:
		if i in B:
			print('Yes')
			break
else:
	print('No')