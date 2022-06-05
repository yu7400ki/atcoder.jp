N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

b = 0
c = 0
cnt = 0
for i in range(N):
	while A[i] >= B[b]:
		b += 1
		if b >= N:
			print(cnt)
			exit()
	while B[b] >= C[c]:
		c += 1
		if c >= N:
			print(cnt)
			exit()
	b += 1
	c += 1
	cnt += 1
	if b >= N or c >= N:
		print(cnt)
		exit()

print(i+1)