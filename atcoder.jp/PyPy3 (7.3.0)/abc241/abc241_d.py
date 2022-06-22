Q = int(input())

A = []
flag = False
for _ in range(Q):
	query = list(map(int, input().split()))
	if query[0] == 1:
		x = int(query[1])
		A.append(x)
		flag = True

	elif query[0] == 2:
		if flag:
			A.sort()
			flag = False
		x, k = query[1], query[2]
		k -= 1
		ok = -1
		ng = len(A)
		while abs(ng - ok) > 1:
			mid = (ok+ng) // 2
			if A[mid] <= x:
				ok = mid
			else:
				ng = mid
		if ok == -1 or ok - k < 0:
			print(-1)
		else:
			print(A[ok-k])

	elif query[0] == 3:
		if flag:
			A.sort()
			flag = False
		x, k = query[1], query[2]
		k -= 1
		ok = len(A)
		ng = -1
		while abs(ng - ok) > 1:
			mid = (ok+ng) // 2
			if A[mid] >= x:
				ok = mid
			else:
				ng = mid
		if ok == -1 or ok + k >= len(A):
			print(-1)
		else:
			print(A[ok+k])