from bisect import bisect_right, insort_left

Q = int(input())

A = []
for _ in range(Q):
	query = list(map(int, input().split()))
	if query[0] == 1:
		x = int(query[1])
		insort_left(A, x)
		continue

	x, k = query[1], query[2]
	k -= 1

	if query[0] == 2:
		ok = bisect_right(A, x)
		ok -= 1
		if ok == -1 or ok - k < 0:
			print(-1)
		else:
			print(A[ok-k])

	elif query[0] == 3:
		ok = bisect_right(A, x)
		if ok == -1 or ok + k >= len(A):
			print(-1)
		else:
			print(A[ok+k])