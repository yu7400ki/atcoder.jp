N, M = map(int,input().split())

a = 0
b = 0

for i in range(N):
	s = input().count('1')
	if s % 2 == 0:
		a += 1
	else:
		b += 1

print(a*b)