H, W = map(int,input().split())

a = []
b = []

for h in range(H):
	s = input()
	if 'o' in s:
		if s.count('o') == 1:
			if a == []:
				a = [s.index('o'), h]
			else:
				b = [s.index('o'), h]
		else:
			a = [s.index('o'), h]
			b = [s.rfind('o'), h]
			break

c = abs(a[0] - b[0])
d = abs(a[1] - b[1])

print(c+d)