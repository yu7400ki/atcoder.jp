N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0
for i in range(N):
	if A[i] == B[i]:
		cnt += A[i]
	elif A[i] < B[i]:
		cnt += A[i]
		a = min(B[i] - A[i], A[i+1])
		A[i+1] -= a
		cnt += a
	elif A[i] > B[i]:
		cnt += B[i]

print(cnt)