N = int(input())
A = list(map(int,input().split()))

P = 0

field = [0,0,0,0]

for i in range(N):
	field[0] = 1
	temp = [0,0,0,0]
	a = A[i]
	for j in range(4):
		if field[j]:
			if j + a < 4:
				temp[j+a] = 1
			else:
				P += 1
	field = temp[:]

print(P)