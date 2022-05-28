H, W = map(int,input().split())

a = []
b = []

for h in range(H):
	s = input()
	if 'o' in s:
		if a == []:
			a = [s.index('o'), h]
		else:
			b = [s.index('o'), h]

c = abs(a[0] - b[0])
d = abs(a[1] - b[1])

print(c+d)