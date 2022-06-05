N = int(input())
A = list(map(int,input().split()))

def accumulate(l):
	res = [0] * (len(l) + 1)
	for i, n in enumerate(l):
		res[i+1] = res[i] + n
	return res

accum_A = accumulate(A)

def bin_search(ok,ng):
	while abs(ng - ok) > 1:
		mid = (ok+ng) // 2
		if accum_A[mid] <= accum_A[-1] // 2:
			ok = mid
		else:
			ng = mid
	return ok

mid = bin_search(0, N)
if abs(accum_A[-1] / 2 - accum_A[mid+1]) < abs(accum_A[-1] / 2 - accum_A[mid]):
	mid = mid+1

print(abs(2*accum_A[mid] - accum_A[-1]))