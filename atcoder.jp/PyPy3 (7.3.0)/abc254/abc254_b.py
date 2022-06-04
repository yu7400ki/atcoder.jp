N = int(input())
A = [1]
print(*A)
for i in range(1,N):
	if i == 1:
		A = [1,1]
		print(*A)
		continue
	A = [1] + [A[j] + A[j+1] for j in range(i-1)] + [1]
	print(*A)