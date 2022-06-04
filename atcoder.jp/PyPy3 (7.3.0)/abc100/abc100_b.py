D, N = map(int,input().split())

if D == 0:
	if N == 100:
		print(101)
	else:
		print(N)
else:
	print(100**D*N)