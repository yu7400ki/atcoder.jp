N, W = map(int,input().split())
A = list(map(int,input().split()))

s = set()
for i in range(N):
	n = A[i]
	if n <= W:
		s.add(n)
	for j in range(i+1,N):
		n = A[i] + A[j]
		if n <= W:
			s.add(n)
		for k in range(j+1,N):
			n = A[i] + A[j] + A[k]
			if n <= W:
				s.add(n)

print(len(s))