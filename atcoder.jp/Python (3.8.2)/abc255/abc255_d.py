N, Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

def accumulate(l):
	res = [0] * (len(l) + 1)
	for i, n in enumerate(l):
		res[i+1] = res[i] + n
	return res

A_accum = accumulate(A)

def bin_search(ok,ng):
	while abs(ng - ok) > 1:
		mid = (ok+ng) // 2
		if A[mid] < x:
			ok = mid
		else:
			ng = mid
	return ok

for _ in range(Q):
	x = int(input())
	X = x * N
	ok = bin_search(-1,N)
	if ok == -1 or ok == N-1:
		print(abs(A_accum[-1]-X))
	else:
		print(abs((A_accum[ok+1] - (x * (ok+1)))) + (A_accum[-1] - A_accum[ok+1] - x * (N - ok-1)))
		#print(abs((A_accum[ok+1] - x)), (A_accum[-1] - A_accum[ok+1] - x * (N - ok-1)))