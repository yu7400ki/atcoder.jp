from bisect import insort_left

Q = int(input())
half = 10**18 // 2

def binary_search(ok,ng,func):
	while abs(ng - ok) > 1:
		mid = (ok+ng) // 2
		if func(mid):
			ok = mid
		else:
			ng = mid
	return ok

A = []
for _ in range(Q):
	query = list(map(int, input().split()))
	if query[0] == 1:
		x = int(query[1]) - half
		insort_left(A, x)
		continue

	x, k = query[1], query[2]
	x -= half
	k -= 1

	if query[0] == 2:
		ok = binary_search(-1, len(A), lambda i: A[i] <= x)
		if ok == -1 or ok - k < 0:
			print(-1)
		else:
			print(A[ok-k]+half)

	elif query[0] == 3:
		ok = binary_search(len(A), -1, lambda i: A[i] >= x)
		if ok == len(A) or ok + k >= len(A):
			print(-1)
		else:
			print(A[ok+k]+half)